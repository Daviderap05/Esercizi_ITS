package com.its.prodotti2.mapper;

import java.util.ArrayList;
import java.util.Collection;

import com.its.prodotti2.dto.ProdottoDTO;
import com.its.prodotti2.dto.ProdottoNoIdDTO;
import com.its.prodotti2.dto.ReportDTO;
import com.its.prodotti2.entity.Prodotto;

public class Mapper {

    public static Prodotto daProdottoDTOAProdotto(ProdottoDTO pDto) {
        return new Prodotto(pDto.getId(), pDto.getMarca(), pDto.getModello(), pDto.getDescrizione(),
                pDto.getCategoria(), pDto.getPrezzoCons(), pDto.getPrezzoMax(), pDto.getQtaDisp());
    }

    public static ProdottoDTO daProdottoAProdottoDTO(Prodotto p) {
        return new ProdottoDTO(p.getId(), p.getMarca(), p.getModello(), p.getDescrizione(), p.getCategoria(),
                p.getPrezzoCons(), p.getPrezzoMax(), p.getQtaDisp());
    }

    public static Prodotto daProdottoNoIdDTOAProdotto(ProdottoNoIdDTO pDto) {
        return new Prodotto(null, pDto.getMarca(), pDto.getModello(), pDto.getDescrizione(), pDto.getCategoria(),
                pDto.getPrezzoCons(), pDto.getPrezzoMax(), pDto.getQtaDisp());
    }

    public static ProdottoNoIdDTO daProdottoAProdottoNoIdDTO(Prodotto p) {
        return new ProdottoNoIdDTO(p.getMarca(), p.getModello(), p.getDescrizione(), p.getCategoria(),
                p.getPrezzoCons(), p.getPrezzoMax(), p.getQtaDisp());
    }

    public static ReportDTO generaReportDaProdotti(Collection<Prodotto> prodotti) {

        ReportDTO report = new ReportDTO();

        if (prodotti.isEmpty()) {
            report.setsommaPezziInMagaz(0);
            report.setProdNonDisp(0);
            report.setMediaPrezziCons(0.0);

            return report;
        }

        Double sommaPrezzoCons = 0.0;
        int sommaPezziInMagaz = 0;
        int prodNonDisp = 0;

        for (Prodotto p : prodotti) {
            report.getListaDescr().add(p.getDescrizione());
            sommaPezziInMagaz += p.getQtaDisp();

            if (p.getPrezzoCons() != null)
                sommaPrezzoCons += p.getPrezzoCons();
            else
                sommaPrezzoCons += 0.0;

            if (p.getQtaDisp() == 0) {
                prodNonDisp++;
                report.getModProdNonDisp().add(p.getModello());
            }

            // Opzionale
            // --------------------------------------------------------------------------------

            String categoriaCorrente = p.getCategoria();
            String idProdCorrente = p.getId();

            if (report.getElencoIdProdPerCat().containsKey(categoriaCorrente)) {
                report.getElencoIdProdPerCat().get(categoriaCorrente).add(idProdCorrente);
            } else {
                ArrayList<String> listaId = new ArrayList<>();
                listaId.add(idProdCorrente);
                report.getElencoIdProdPerCat().put(categoriaCorrente, listaId);
            }

            // --------------------------------------------------------------------------------

        }

        report.setsommaPezziInMagaz(sommaPezziInMagaz);
        report.setProdNonDisp(prodNonDisp);
        report.setMediaPrezziCons(sommaPrezzoCons / prodotti.size());

        return report;
    }
}

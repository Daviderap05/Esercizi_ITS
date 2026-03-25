package com.factory;

import java.util.List;

public interface DataExport {
    void export(List<String> data, String fileName);

    String getMime();
}

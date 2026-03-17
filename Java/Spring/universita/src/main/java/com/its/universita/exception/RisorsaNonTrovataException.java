package com.its.universita.exception;

import org.springframework.http.HttpStatus;
import org.springframework.web.bind.annotation.ResponseStatus;

// Appena questa eccezione viene lanciata, Spring restituisce in automatico un errore 404
@ResponseStatus(HttpStatus.NOT_FOUND)
public class RisorsaNonTrovataException extends RuntimeException {
    
    public RisorsaNonTrovataException(String message) {
        super(message);
    }
}
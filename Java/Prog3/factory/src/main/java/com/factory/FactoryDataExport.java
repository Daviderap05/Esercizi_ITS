package com.factory;

import java.lang.reflect.InvocationTargetException;
import java.lang.reflect.Method;

public class FactoryDataExport {
    @SuppressWarnings("CallToPrintStackTrace")
    public static DataExport getExporter(String className) {
        try {
            Class<?> clazz = Class.forName(className);
            Method method = clazz.getDeclaredMethod("getInstance");
            return (DataExport) method.invoke(null);
        } catch (ClassNotFoundException | IllegalAccessException | NoSuchMethodException | SecurityException
                | InvocationTargetException e) {
            e.printStackTrace();
            return null;
        }
    }
}
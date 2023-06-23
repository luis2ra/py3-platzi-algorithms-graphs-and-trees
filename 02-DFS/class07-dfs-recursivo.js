const dfs =  function(raiz, valorAEncontrar) {
    console.log("En este momento estoy en el nodo que tiene el valor ", raiz.valor);
    if (raiz.valor === valorAEncontrar) {
        console.log("Encontre el valor!!!");
        return raiz
    }
    /**
     * Esto aplica para el caso de un arbol binario
     */
    izquierda = dfs(raiz.izquierda, valorAEncontrar);
    derecha = dfs(raiz.derecha, valorAEncontrar);
    if (izquierda != null) {
        return izquierda
    }
    if (derecha != null) {
        return derecha
    }

    /**
     * Esto aplica para el caso general
     */
    
    /**
    for(var i = 0; i < raiz.hijos.length; i++) {
        var nodoResultado = dfs(raiz, hijos[i], valorAEncontrar);
        if (nodoResultado != null) {
            return nodoResultado;
        }
    }
    */
    return null;
}

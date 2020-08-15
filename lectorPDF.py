import os
from PyPDF2 import PdfFileReader

    



class lectorPDF:
    PDFText = []
    PDFALL = ""
    tmpBufferLineas = []
    Ruta = ""

    def cargarPaginas(self):
        for inx in self.PDFText:
            self.PDFALL += inx


    def cargarArchivo(self, ruta):
        self.Ruta = ruta
        with open(ruta, 'rb') as f:
            archivoPDF = PdfFileReader(f)
            for pagina in range(archivoPDF.getNumPages()):
                self.PDFText.append(archivoPDF.getPage(pagina).extractText())
        self.cargarPaginas()


    def cantPaginas(self):
        return "La cantidad de paginas del documento es: {}".format(len(self.PDFText))

    def rutaActual(self):
        return "La ruta del actual documento es: {}".format(self.Ruta)
    
    def imprimirPagina(self, numPagina):
        if numPagina <= (len(self.PDFText) +1):
            return self.PDFText[numPagina - 1]
        else:
            return "Error: Fuera del indice." 

    def crearSeparador(self, separador, pagina="Todas", almacenar=False):
        resultado = []
        if pagina == "Todas":
            resultado.append(self.PDFALL.split(separador))
        else:
            resultado = self.PDFText[pagina - 1].split(separador)
            return resultado
        if almacenar==True:
            self.tmpBufferLineas = resultado
        return resultado


class OrdenDeCompra:    
    __codigo = []
    __descripcion = []
    __cantidad = []
    __precio_unitario = []
    
    CabeceraRemito = {
    'fecha_emision' : '',
    'fecha_entrega' : '',
    'referencia_oc'    : '',
    'cliente'       : '',
    'campaña'       : '',
    'circuito'      : '',
    'lineas'        : 0 ,
    }

    def setCodigo(self, codigo_completo):
        codigo_completo  = codigo_completo.split(" ")[1]
        self.__codigo.append(codigo_completo)

    def setDescripcion(self, descripcion):
        descripcion = descripcion.strip()
        self.__descripcion.append(descripcion)

    def setCantidad(self, cantidad):
        cantidad = cantidad.replace(".", "")
        int_cantidad = int(cantidad)
        self.__cantidad.append(int_cantidad)
    
    def setPrecioUnit(self, precio_unitario):
        precio_unitario = precio_unitario.replace(",", ".")
        float_precio_unitario = float(precio_unitario)
        self.__precio_unitario.append(float_precio_unitario)

    def getRegistros(self):
        tmpDict = {}
        self.CabeceraRemito['lineas'] = len(self.__codigo)
        tmpDict['cabecera'] = self.CabeceraRemito
        for index, codigo in enumerate(self.__codigo):
            tmp = {}
            tmp['descripcion'] = self.__descripcion[index]
            tmp['cantidad'] = self.__cantidad[index]
            tmp['precio_unitario'] = self.__precio_unitario[index]
            tmpDict[index] = tmp 
        return tmpDict



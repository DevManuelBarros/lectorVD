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
    __fecha_entrega = []


    CabeceraOrdenDeCompra = {
    'fecha_emision' : '',
    'referencia_oc'    : '',
    'cliente'       : '',
    'campaña'       : '',
    'circuito'      : '',
    'lineas'        : 0 ,
    'actualizar'    : 0 ,
    'version'       : 1
    }

    def setCodigo(self, codigo_completo):
        if ' ' in codigo_completo: 
            codigo_completo  = codigo_completo.split(" ")[1]

        self.__codigo.append(codigo_completo)

    def setDescripcion(self, descripcion):
        print(descripcion)
        self.__descripcion.append(descripcion)

    def setCantidad(self, cantidad):
        if not isinstance(cantidad, int):
            cantidad = cantidad.replace(".", "")
            int_cantidad = int(cantidad)
            self.__cantidad.append(int_cantidad)
        else:
            self.__cantidad.append(cantidad)
    
    def setPrecioUnit(self, precio_unitario):
        print(precio_unitario)
        if isinstance(precio_unitario, str):
            precio_unitario = precio_unitario.replace(",", ".")
            self.__precio_unitario.append(float(precio_unitario))
        if isinstance(precio_unitario, float):
            self.__precio_unitario.append(precio_unitario)

    def setFechaEntrega(self, fecha_entrega):
        if '/' in fecha_entrega:
            fecha_entrega = fecha_entrega.replace('/', '-')
        self.__fecha_entrega.append(fecha_entrega)


    def getRegistros(self):
        tmpDict = {}
        self.CabeceraOrdenDeCompra['lineas'] = len(self.__codigo)
        tmpDict['cabecera'] = self.CabeceraOrdenDeCompra
        for index, codigo in enumerate(self.__codigo):
            tmp = {}
            tmp['codigo'] = codigo
            tmp['descripcion'] = self.__descripcion[index]
            tmp['cantidad'] = self.__cantidad[index]
            tmp['precio_unitario'] = self.__precio_unitario[index]
            tmp['fecha_entrega'] = self.__fecha_entrega[index]
            tmpDict[index] = tmp 
        return tmpDict



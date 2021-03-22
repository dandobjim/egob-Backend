from egob.config import settings
from egob.logger import logger
from SPARQLWrapper import SPARQLWrapper, JSON


class Virtuoso:
    @staticmethod
    def create_id():
        sparql = SPARQLWrapper("http://192.168.213.38:8086/sparql")
        sparql.setQuery("""
                PREFIX ter:   <http://www.datos.misiones.gob.ar/ontologias/gobierno/ar.gp.N.territorio.owl#>
                PREFIX tys:   <http://www.datos.misiones.gob.ar/ontologias/gobierno/ejecutivo/ar.gp.N.pe.tys.owl#>
                PREFIX infra: <http://www.datos.misiones.gob.ar/ontologias/gobierno/ejecutivo/ar.gp.N.pe.infraestructura.owl#>
                PREFIX osm:   <http://www.datos.misiones.gob.ar/ontologias/gobierno/osm.owl#>
                PREFIX foaf:  <http://www.datos.misiones.gob.ar/ontologias/gobierno/ejecutivo/ar.gp.N.pe.foaf.owl#>
                PREFIX gn:    <http://www.geonames.org/#>
                PREFIX map:   <http://www.datos.misiones.gob.ar/ontologias/mapillary.owl#>
                PREFIX ec: <http://www.datos.misiones.gob.ar/ontologias/gobierno/ejecutivo/ar.gp.N.pe.ec.owl#>
                
                SELECT distinct ?domicilio ?edificio ?responsable ?telefono ?latitud ?longitud
                WHERE {
                GRAPH <egob> { 
                ?Tramite tys:ID "New_ID_Card"^^<http://www.w3.org/2001/XMLSchema#string> .
                ?Tramite tys:IsMadeIn ?TipoLugar .
                ?Lugar rdf:type ?TipoLugar .
                ?Lugar infra:Place ter:Posadas .
                ?Lugar infra:Address ?domicilio .
                ?Lugar infra:phone ?telefono .
                ?Lugar infra:BuildingName ?edificio .
                ?lugar infra:ResponsiblePerson ?foafResponsable .
                ?foafResponsable ec:Name ?responsable .
                ?osm osm:street ?domicilio .
                ?osm osm:lat ?latitud .
                ?osm osm:long ?longitud
                }
                }
                    """)
        sparql.setReturnFormat(JSON)
        results = sparql.query().convert()
        data = []
        for result in results["results"]["bindings"]:
            data.append(result)
        return data

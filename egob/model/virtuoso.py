from egob.config import settings
from egob.logger import logger
from SPARQLWrapper import SPARQLWrapper, JSON


class Virtuoso:
    @staticmethod
    def create_id(id: str):
        sparql = SPARQLWrapper("http://192.168.213.38:8086/sparql")
        sparql.setQuery(f"""
                PREFIX ter:   <http://www.datos.misiones.gob.ar/ontologias/gobierno/ar.gp.N.territorio.owl#>
                PREFIX tys:   <http://www.datos.misiones.gob.ar/ontologias/gobierno/ejecutivo/ar.gp.N.pe.tys.owl#>
                PREFIX infra: <http://www.datos.misiones.gob.ar/ontologias/gobierno/ejecutivo/ar.gp.N.pe.infraestructura.owl#>
                PREFIX osm:   <http://www.datos.misiones.gob.ar/ontologias/gobierno/osm.owl#>
                PREFIX foaf:  <http://www.datos.misiones.gob.ar/ontologias/gobierno/ejecutivo/ar.gp.N.pe.foaf.owl#>
                PREFIX gn:    <http://www.geonames.org/#>
                PREFIX map:   <http://www.datos.misiones.gob.ar/ontologias/mapillary.owl#>
                PREFIX ec: <http://www.datos.misiones.gob.ar/ontologias/gobierno/ejecutivo/ar.gp.N.pe.ec.owl#>

                SELECT distinct ?domicilio ?edificio ?responsable ?telefono ?coordinates
                WHERE {{
                GRAPH <egob> {{ 
                    ?Tramite tys:ID "{id}"^^<http://www.w3.org/2001/XMLSchema#string> .
                    ?Tramite tys:IsMadeIn ?TipoLugar .
                    ?Lugar rdf:type ?TipoLugar .
                    OPTIONAL{{?Lugar infra:Address ?domicilio .}}
                    OPTIONAL{{?Lugar infra:phone ?telefono .}}
                    OPTIONAL{{?Lugar infra:BuildingName ?edificio .}}
                    OPTIONAL{{?lugar infra:ResponsiblePerson ?foafResponsable .}}
                    OPTIONAL{{?Lugar infra:Coordinates ?coordinates}}
                    OPTIONAL{{?foafResponsable ec:Name ?responsable .}}                   
                }}
        }}
                    """)
        sparql.setReturnFormat(JSON)
        results = sparql.query().convert()
        logger.info("RESULTS")
        logger.info(results)
        data = []
        for result in results["results"]["bindings"]:
            data.append(result)
        logger.info("DATA")
        logger.info(data)
        return data

from SPARQLWrapper import JSON, SPARQLWrapper

sparql = SPARQLWrapper("http://dbpedia.org/sparql")

query = """
PREFIX dbo: <http://dbpedia.org/ontology/>
PREFIX dbp: <http://dbpedia.org/property/>
PREFIX dbr: <http://dbpedia.org/resource/>

SELECT ?diseaseName GROUP_CONCAT(?medicalDiagnosisName; separator=", ") AS ?medicalDiagnosisNames
WHERE {
    ?disease a dbo:Disease .
    ?disease dbp:name ?diseaseName .
    FILTER (lang(?diseaseName) = "en") .
    ?disease dbp:field dbr:Gastroenterology .
    ?disease dbo:medicalDiagnosis ?medicalDiagnosis .
    ?medicalDiagnosis dbp:name ?medicalDiagnosisName .
    FILTER (lang(?medicalDiagnosisName) = "en") .
}
"""

sparql.setQuery(query)
sparql.setReturnFormat(JSON)

results = sparql.query().convert()

for result in results["results"]["bindings"]:
    disease = result["diseaseName"]["value"]
    diagnosis_methods = result["medicalDiagnosisNames"]["value"]

    print(f"Disease: {disease}")
    print(f"Diagnosis methods: {diagnosis_methods}")
    print()

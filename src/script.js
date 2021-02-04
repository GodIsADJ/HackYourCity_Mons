function fetched(){
	let data = []
fetch('https://www.odwb.be/api/records/1.0/search/?dataset=fetes-et-manifestations-dans-la-ville-de-mons&q=&rows=10&facet=etablissement_nom&facet=classification&facet=etablissement_adresse_1&facet=etablissement_code_postal&facet=etablissement_commune&facet=tarifs&facet=periodes_textuelles&facet=description_fr')
.then(response => response.json())
.then(json => json.records.forEach(element => {
data.push(element.fields)
}))
return data
}

let datas = [fetched()]
console.log(datas[0])
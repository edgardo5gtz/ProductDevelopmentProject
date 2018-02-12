let vm = new Vue({
    el: '#app',
    delimiters: ['${','}'],
    data: () => {
        return {
            risks: "",
            form: {
                risk_name: "",
                risk_type: "",
                fields: [],
                field_types: [
                    "Text",
                    "Number",
                    "Date",
                    "Enum"
                ],
            },
            new_field_type: '',
        }},
    methods: {
        getRisksList:  () => {
            axios.get('/risks_api/risks/')
                .then((response) => {
                    this.error = false;
                    vm.risks = response.data;
                    console.log(response.data);
                })
                .catch((error) => {
                    this.error = true;
                    this.risks = "Ups";
                    console.log(error);
                });
        },
        addRisk: () => {
            vm.postRisk()
        },
        postRisk: () => {
            axios.post('/risks_api/risks/', {
                name: vm.form.risk_name
            }).then((response) =>{
                vm.postRiskType(response.data.id)
            }) .catch(function (error) {
                console.log(error);
            });
        },
        postRiskType: (prev_res) => {
            axios.post('/risks_api/risk_types/', {
                type: vm.form.risk_type,
                risk: prev_res
            }).then((response) =>{
                vm.form.fields.map((item)=>{
                    console.log("Debug map function")
                    console.log(item);
                    vm.postRiskField(item, response.data.id);
                });
            }) .catch(function (error) {
                console.log(error);
            });
        },
        postRiskField: (item, prev_res) => {
            axios.post('/risks_api/risk_fields/', {
                risk_type: prev_res,
                field: item.name
            }).then((response) =>{
                let valURL = vm.valTypeURL(item.type);
                vm.postValue(valURL, response.data.id, item)
            }) .catch(function (error) {
                console.log(error);
            });
        }, postValue: (url, prev_res, item) => {
            axios.post(url, {
                value: item.value,
                risk_field: prev_res
            }).then((response) =>{
                console.log(response)
            }) .catch(function (error) {
                console.log(error);
            });
        },
        valTypeURL: (type) => {
            switch (type){
                case 'Text':
                    return '/risks_api/text_fields/';
                case 'Enum':
                    return '/risks_api/enum_fields/';
                case 'Date':
                    return '/risks_api/date_fields/';
                case 'Number':
                    return '/risks_api/number_fields/';
                default:
                    return 0
            }
        },
        removeField: () => {

        },
        addField () {
            this.form.fields.push({
                name: "",
                type: this.new_field_type,
                value: ""
            });
        }
    }
});


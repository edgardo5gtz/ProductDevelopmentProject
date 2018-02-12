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

        },
        removeField: () => {

        },
        addField () {
            let a = this.new_field_type;
            console.log(a);
            this.form.fields.push({
                name: "",
                type: this.new_field_type,
                value: ""
            });
        }
    }
});


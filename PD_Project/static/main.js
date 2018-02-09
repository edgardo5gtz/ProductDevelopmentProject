let vm = new Vue({
    el: '#app',
    delimiters: ['${','}'],
    data: {
        risks: ""
    },
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
        }
    }
});


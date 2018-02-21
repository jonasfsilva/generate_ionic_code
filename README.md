# generate_ionic_code
Gerador de codigo para providers do Ionic 3, feito em Python


Exemplo de Codigo Gerado Apenas funções por enquanto:

'''
    
    getAll(){
        return new Promisse((resolve, reject) =>  {
 
            let url = this.urlAPI + 'params'

            this.http.get(url)
                .subscribe((result:any) => {
                    resolve(result)
                },
                (error) => {
                    reject(error)
                })
        });
    }
    

    get(id: number){
        return new Promisse((resolve, reject) =>  {

            let url = this.urlAPI + 'users?' + 'id'

            this.http.get(url)
                .subscribe((result:any) => {
                    resolve(result)
                },
                (error) => {
                    reject(error)
                })
        });
    }


    save(user: any){    
        return new Promisse((resolve, reject) =>  {
            let url = this.urlAPI + 'users?'

            this.http.post(url, user)
                .subscribe((result:any) => {
                    resolve(result)
                },
                (error) => {
                    reject(error)
                })
        });
    }



    update(user: any){
        return new Promisse((resolve, reject) =>  {

            let url = this.urlAPI + 'users?' + 'id'

            this.http.put(url, user)
                .subscribe((result:any) => {
                    resolve(result)
                },
                (error) => {
                    reject(error)
                })
        });
    }
'''

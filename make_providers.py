import os
import sys

print('aki')

var = input("Digite o nome do Provider: ")
url_api = input("Digite da url padrao na API: ")
print("{0}Provider".format(str(var)))

# path = '/{0}Provider.js'
# new_days = open(path, 'w')

get_all_text = """
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
"""

get_one_text = """
get(id: number){
    return new Promisse((resolve, reject) =>  {

        let url = this.urlAPI + '%(url_api)s' + 'id'

        this.http.get(url)
            .subscribe((result:any) => {
                resolve(result)
            },
            (error) => {
                reject(error)
            })
    });
}
"""

save_text = """
save(user: any){
    return new Promisse((resolve, reject) =>  {

        let url = this.urlAPI + '%(url_api)s/' + 'id'

        this.http.post(url, user)
            .subscribe((result:any) => {
                resolve(result)
            },
            (error) => {
                reject(error)
            })
    });
}
"""

update_text = """
update(user: any){
    return new Promisse((resolve, reject) =>  {

        let url = this.urlAPI + '%(url_api)s/' + 'id'

        this.http.put(url, user)
            .subscribe((result:any) => {
                resolve(result)
            },
            (error) => {
                reject(error)
            })
    });
}
"""

remove_text = """
delete(id: number){
    return new Promisse((resolve, reject) =>  {

        let url = this.urlAPI + '%(url_api)s/' + 'id'

        this.http.delete(url)
            .subscribe((result:any) => {
                resolve(result)
            },
            (error) => {
                reject(error)
            })
    });
}
"""

data = {
    'url_api':url_api
}

# print(get_all_text)
print(get_one_text % data)
print(save_text % data)
print(update_text % data)


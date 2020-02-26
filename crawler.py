from url import url
import json
import csv

def main():
        print(web_crawling.crawling_1(web_crawling))
        print(web_crawling.crawling_2(web_crawling))

class web_crawling:
    def crawling_1(self):# Rececbe primeira url, organiza e imprime na tela
        page = url.urls_requests(url, 'https://www.vultr.com/pricing/')# url esta sendo redirecionada para https://www.vultr.com/products/cloud-compute/
        list_storage_cpu_memory_bandwidth_price = page.xpath('//strong/text()')

        def imprime_json_csv(list_storage_cpu_memory_bandwidth_price):
            storage = []
            cpu = []
            memory = []
            bandwidth = []
            price = []
            p = 0
            for obj in list_storage_cpu_memory_bandwidth_price:
                if " cpu" in obj.lower():
                    storage.append(str(list_storage_cpu_memory_bandwidth_price[p-1]))
                    cpu.append(str(obj))
                    memory.append(str(list_storage_cpu_memory_bandwidth_price[p+1]))
                    bandwidth.append(str(list_storage_cpu_memory_bandwidth_price[p+2]))
                    price.append(str(list_storage_cpu_memory_bandwidth_price[p+3]))
                p+=1

            p = 0
            lista_json = []

            arq_csv = open('web_crawling_1.csv', 'w')
            writer = csv.writer(arq_csv)
            writer.writerow(('CPU', 'MEMORY', 'STORAGE', 'BANDWIDTH', 'PRICE'))
            print('CPU', 'MEMORY', 'STORAGE', 'BANDWIDTH', 'PRICE')
            for m in memory:
                writer.writerow((cpu[p], m, storage[p], bandwidth[p], price[p]))
                print(cpu[p], m, storage[p], bandwidth[p], price[p])
                lista = {
                    "cpu": cpu[p],
                    "memory": m,
                    "storage": storage[p],
                    "bandwidth": bandwidth[p],
                    "price": price[p]
                }
                p += 1
                lista_json.append(lista)
            arq_csv.close()
            arq = open('web_crawling_1.json', 'w')
            json.dump(lista_json, arq)
            arq.close()

        return imprime_json_csv(list_storage_cpu_memory_bandwidth_price)            

        
    def crawling_2(self):# Rececbe segunda url, organiza e imprime na tela

        page = url.urls_requests(url, 'https://www.digitalocean.com/pricing/')
        list_memory_price = page.xpath('//strong/text()')
        list_vcpus_transfer_ssd = page.xpath('//td/text()')

        vcpus = []
        transfer = []
        ssd = []
        memory = []
        price = []
        p = 0
        for obj1 in list_memory_price:
            if "gb" in obj1.lower():
                memory.append(str(obj1))
            if "mo" in obj1.lower():
                price.append(str(obj1))

        for obj in list_vcpus_transfer_ssd:
            obj = str(obj).replace(" ", "").replace("\n", "")
            if "vcpu" in obj.lower():
                vcpus.append(obj.replace("vCPU", " vCPU"))
            elif "gb" in obj.lower():
                ssd.append(obj.replace("GB", " GB"))
            elif "tb" in obj.lower():
                transfer.append(obj.replace("TB", " TB"))
        

        arq_csv = open('web_crawling_2.csv', 'w')
        writer = csv.writer(arq_csv)
        writer.writerow(('VCPUS', 'MEMORY', 'SSD', 'TRANSFER', 'PRICE'))            
        print("VCPUS", "MEMORY", "SSD", "TRANSFER", "PRICE")
        
        lista_json = []

        for m in memory:
            writer.writerow((vcpus[p], m, ssd[p], transfer[p], price[p]))
            print(vcpus[p], m, ssd[p], transfer[p], price[p])
            lista = {
                "vcpus": vcpus[p],
                "memory": m,
                "ssd": ssd[p],
                "transfer": transfer[p],
                "price": price[p]
            }
            p+=1
            lista_json.append(lista)

        arq_csv.close()
        arq_json = open('web_crawling_2.json', 'w')
        json.dump(lista_json, arq_json)
        arq_json.close()
    


main()
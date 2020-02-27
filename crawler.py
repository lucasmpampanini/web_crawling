from url import url
import json
import csv
import sys

def main():
    comando = sys.argv[1]

    if comando == crawling_1.nome_crawler:
        crawling_1.imprime(crawling_1)
        crawling_1.save_json(crawling_1)
        crawling_1.save_csv(crawling_1)
    if comando == crawling_2.nome_crawler:
        crawling_2.imprime(crawling_2)
        crawling_2.save_json(crawling_2)
        crawling_2.save_csv(crawling_2)


class crawling_1:
    def __init__(self, cpu, memory, storage, bandwidth, price):
        self.cpu = cpu
        self.memory = memory
        self.storage = storage
        self.bandwidth = bandwidth
        self.price = price

    page = url.urls_requests(url, 'https://www.vultr.com/pricing/')# url esta sendo redirecionada para https://www.vultr.com/products/cloud-compute/
    list_storage_cpu_memory_bandwidth_price = page.xpath('//strong/text()')

    nome_crawler = "crawler_1" #nome do crawler, que é colocado no shell "python3 crawler.py crawler_1"

    cpu = []
    memory = []
    storage = []
    bandwidth = []
    price = []
    p = 0
    for obj in list_storage_cpu_memory_bandwidth_price:
        if " cpu" in obj.lower():
            storage.append(str(list_storage_cpu_memory_bandwidth_price[p-1]))
            cpu.append(str(obj))
            memory.append(str(list_storage_cpu_memory_bandwidth_price[p+1]))
            bandwidth.append(str(list_storage_cpu_memory_bandwidth_price[p+2]))
            price.append(str(list_storage_cpu_memory_bandwidth_price[p+3])+'/mo')
        p+=1

    def imprime(self):# Rececbe itens da primeira pagina, organiza para imprimir na tela
        p = 0
        print('CPU', 'MEMORY', 'STORAGE', 'BANDWIDTH', 'PRICE')
        for m in crawling_1.memory:
            print(crawling_1.cpu[p], m, crawling_1.storage[p], crawling_1.bandwidth[p], crawling_1.price[p])
            p += 1

    def save_json(self):# Rececbe itens da primeira pagina, organiza para salvar em json
        p = 0
        lista_json = []
        for m in crawling_1.memory:
            lista = {
                     "cpu": crawling_1.cpu[p],
                     "memory": m,
                     "storage": crawling_1.storage[p],
                     "bandwidth": crawling_1.bandwidth[p],
                     "price": crawling_1.price[p]
                   }
            p += 1
            lista_json.append(lista)
        arq = open('web_crawling_1.json', 'w')
        json.dump(lista_json, arq)
        arq.close()

    def save_csv(self):# Rececbe itens da primeira pagina, organiza para salvar em csv
        p = 0
        arq = open('web_crawling_1.csv', 'w')
        writer = csv.writer(arq)
        writer.writerow(('CPU', 'MEMORY', 'STORAGE', 'BANDWIDTH', 'PRICE'))
        for m in crawling_1.memory:
            writer.writerow((crawling_1.cpu[p], m, crawling_1.storage[p], crawling_1.bandwidth[p], crawling_1.price[p]))
            p+=1
        arq.close()

       

class crawling_2:
    def __init__(self, vcpus, memory, ssd, transfer, price):
        self.vcpus = vcpus
        self.memory = memory
        self.ssd = ssd
        self.transfer = transfer
        self.price = price
   

    nome_crawler = "crawler_2"#nome do crawler, que é colocado no shell "python3 crawler.py crawler_2"

    page = url.urls_requests(url, 'https://www.digitalocean.com/pricing/')
    list_memory_price = page.xpath('//strong/text()')
    list_vcpus_transfer_ssd = page.xpath('//td/text()')

    vcpus = []
    transfer = []
    ssd = []
    memory = []
    price = []
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
        
    def imprime(self):# Rececbe itens da segunda pagina, organiza para imprimir na tela
        print("VCPUS", "MEMORY", "SSD", "TRANSFER", "PRICE")
        p = 0
        for m in crawling_2.memory:
            print(crawling_2.vcpus[p], m, crawling_2.ssd[p], crawling_2.transfer[p], crawling_2.price[p])
            p+=1

    def save_json(self):# Rececbe itens da segunda pagina, organiza para salvar em json
        lista_json = []
        p = 0
        for m in crawling_2.memory:
            lista = {
                "vcpus": crawling_2.vcpus[p],
                "memory": m,
                "ssd": crawling_2.ssd[p],
                "transfer": crawling_2.transfer[p],
                "price": crawling_2.price[p]
            } 
            p+=1
            lista_json.append(lista)
        arq = open('web_crawling_2.json', 'w')
        json.dump(lista_json, arq)
        arq.close()

    def save_csv(self):# Rececbe itens da segunda pagina, organiza para salvar em csv
        p = 0
        arq = open('web_crawling_2.csv', 'w')
        writer = csv.writer(arq)
        writer.writerow(('VCPUS', 'MEMORY', 'SSD', 'TRANSFER', 'PRICE'))  
        for m in crawling_2.memory:
            writer.writerow((crawling_2.vcpus[p], m, crawling_2.ssd[p], crawling_2.transfer[p], crawling_2.price[p]))
            p+=1

        arq.close()
        
main()
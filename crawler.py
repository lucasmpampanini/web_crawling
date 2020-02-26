from url import url
import json
import csv

def main():
        print(web_crawling.crawling_1(web_crawling))


class web_crawling:
    def crawling_1(self):# Rececbe primeira url, organiza e imprime na tela
        page = url.urls_requests(url, 'https://www.vultr.com/pricing/')# url esta sendo redirecionada para https://www.vultr.com/products/cloud-compute/
        list_storage_cpu_memory_bandwidth_price = page.xpath('//strong/text()')

        def imprime_json(list_storage_cpu_memory_bandwidth_price):
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
            listaok = []

            arq_csv = open('web_crawling_1.csv', 'w')
            writer = csv.writer(arq_csv)
            writer.writerow(('cpu', 'memory', 'storage', 'bandwidth', 'price'))
            print("cpu", "memory", "storage", "bandwidth", "price")
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
                listaok.append(lista)
            arq_csv.close()
            arq = open('web_crawling_1.json', 'w')
            json.dump(listaok, arq)
            arq.close()            

            

        return imprime_json(list_storage_cpu_memory_bandwidth_price)

main()
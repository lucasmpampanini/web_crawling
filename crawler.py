from url import url

def main():
        print(web_crawling.crawling_1(web_crawling))



class web_crawling:
    def crawling_1(self):
        page = url.urls_requests(url, 'https://www.vultr.com/pricing/')
        list_storage_cpu_memory_bandwidth_price = page.xpath('//strong/text()')

        storage = []
        cpu = []
        memory = []
        bandwidth = []
        price = []
        p = 0
        for obj in list_storage_cpu_memory_bandwidth_price:
            if " cpu" in obj.lower():
                storage.append(list_storage_cpu_memory_bandwidth_price[p-1])
                cpu.append(obj)
                memory.append(list_storage_cpu_memory_bandwidth_price[p+1])
                bandwidth.append(list_storage_cpu_memory_bandwidth_price[p+2])
                price.append(list_storage_cpu_memory_bandwidth_price[p+3])
            p+=1

        p = 0
        print("cpu", "storage", "bandwidth", "price")
        for m in memory:
            print(cpu[p], m, storage[p], bandwidth[p], price[p])
            p += 1

main()
#Name : Ashutosh Anil Deshpande Student ID : 201758974

#Initializing Global Variables to store cache,requests and frequency
cache = []
requests = []
cache_dic = {}
frequency_list = {}


def add_pages():
    while True:
        page = int(input("Enter request page number:"))
        requests.append(page)
        if page == 0:
            break


def fifo():
    #Fifo Cache algorithm
    for pages in requests:
        if pages == 0:
            break
        elif pages not in cache and len(cache)==8:
            cache.pop(0)
            cache.append(pages)
            print("miss")
        elif pages in cache:
            print("hit")
        elif pages not in cache and len(cache) < 8:
            print("miss")
            cache.append(pages)
    print(f"The final state of  cache is : {cache}")
    print(f"The user entered requests are : {requests}")
    cache.clear()


def lfu():
   #LFU cache algorithm
    for pages in requests:
        if pages == 0:
            break
        elif pages in cache_dic:
            print("hit")
            cache_dic[pages] += 1
            frequency_list[pages] += 1
        elif pages not in cache_dic and pages in frequency_list:
            print("miss")
            if len(cache_dic) == 8:
                min_cache_dic = min(cache_dic.values())
                minkey_cache_dic = [key for key in cache_dic if cache_dic[key] == min_cache_dic]
                page_to_remove = min(minkey_cache_dic)
                cache_dic.pop(page_to_remove)
            frequency_list[pages] += 1
            cache_dic.update({pages: frequency_list[pages]})
        elif pages not in cache_dic and pages not in frequency_list:
            print("miss")
            if len(cache_dic) == 8:
                min_cache_dic = min(cache_dic.values())
                minkey_cache_dic = [key for key in cache_dic if cache_dic[key] == min_cache_dic]
                page_to_remove = min(minkey_cache_dic)
                cache_dic.pop(page_to_remove)
            cache_dic[pages] = 1
            frequency_list[pages] = 1
    x = cache_dic.keys()
    print(f"The final state of cache is :{x}")
    print(f"The user entered requests are :{requests}")
    cache_dic.clear()

  #Loop to take inputs
while True:
    add_pages()
    user_input = input(
        "Enter 1 for FIFO \n"
        "Enter 2 for LFU \n"
        "Enter Q to Quit: "
        )
    if user_input == "1":
        fifo()
    elif user_input == "2":
        if requests == []:
            lfu()
        else:
            del requests[-1]
            lfu()
    
    elif user_input == "Q":
        print("You have exited the program.")
        break
    else:
        print("Invalid input. Please choose a valid option.")
    requests.clear()
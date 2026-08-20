# import time

# # sync
# print("--"*30)

# def cricket_data():
#     print("fetching cricket data....")
#     cricket_data_time=time.sleep(9)
#     print("cricket_data_fetched_successfully")
    
    
    
# def news_data():
#     print("fetching news data....")
#     news_data_time = time.sleep(4)  # create the simulated time 
#     print("news_data_fetched_successfully")
    
    
# def main():
#     start_time = time.time()
    
#     cricket_data()
#     news_data()
    
#     end_time = time.time()
#     print(f"total time taking is {end_time}-{start_time} seconds")
    
# main()



# async

import asyncio
import time

async def cricket_data():
    print("fetching cricket data....")
    await asyncio.sleep(9)
    print("cricket_data_fetched_successfully")

async def news_data():
    print("fetching news data....")
    await asyncio.sleep(4)
    print("news_data_fetched_successfully")

async def main():
    start_time = time.time()

    await asyncio.gather(
        cricket_data(),
        news_data()
    )

    end_time = time.time()
    print(f"total time taken is {end_time - start_time} seconds")

asyncio.run(main())
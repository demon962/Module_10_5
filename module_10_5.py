from multiprocessing import Pool
import time

def read_info(name):
    all_data = []

    with open(name, 'r') as file:
        while True:
            line = file.readline().strip()

            if not line:
                break

            all_data.append(line)

    return all_data


file_names = [f'./file_{number}.txt' for number in range(1, 5)]

if __name__ == '__main__':
    start_time = time.time()

    with Pool(processes=len(file_names)) as pool:
        results = pool.map(read_info, file_names)

    print(f'Параллельное выполнение заняло {time.time() - start_time:.4f} секунд')
import random
import string

from utils.warehouse_gpu import WarehouseGPU

warehouse_gpu = WarehouseGPU()

print(warehouse_gpu.gpu().get_all())
print(warehouse_gpu.gpu().get_all_only_name())
print(warehouse_gpu.gpu().get_all_name_vendor_device())
print(warehouse_gpu.gpu().get_all_by_id(random.randint(1, 857)))
print(warehouse_gpu.gpu().get_name_mobile_part_by_mobile_part(random.randint(0, 2)))

print(warehouse_gpu.warehouse().get_all())
print(warehouse_gpu.warehouse().get_all_by_zone(random.choice(string.ascii_letters)))
print(warehouse_gpu.warehouse().get_all_by_smaller_price(random.randint(7000, 35000)))
print(warehouse_gpu.warehouse().get_all_have())

print(warehouse_gpu.warehouse_gpu().get_all_gpu_by_zone(random.choice(string.ascii_letters)))
print(warehouse_gpu.warehouse_gpu().get_name_zone_by_zone(random.choice(string.ascii_letters)))


warehouse_gpu.warehouse().create_new_warehouse(product_id=random.randint(1, 857), quantity=random.randint(1, 100))

import psutil


memory = psutil.virtual_memory()


total_memory = memory.total / (1024**3)
available_memory = memory.available / (1024**3)
used_memory = memory.used / (1024**3)


# templ = "%-17s %8s %8s %8s %5s%% %9s  %s"
# print(templ % ("Memory", "Total", "Used", "Free", "Use ", "Type", "Mount"))


print(f"Общий объем памяти: {total_memory:.2f} ГБ")
print(f"Доступно памяти: {available_memory:.2f} ГБ")
print(f"Используется памяти: {used_memory:.2f} ГБ")

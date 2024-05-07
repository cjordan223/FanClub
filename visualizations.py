import matplotlib.pyplot as plt

def plot_disk_usage(disk_data, output_path):
    #disk usage
    labels = ['Free Space', 'Used Space']
    sizes = [disk_data['free'], disk_data['used']]

    plt.figure(figsize=(6, 6))
    plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140)
    plt.axis('equal')
    plt.title('Disk Usage Breakdown')
    plt.savefig(output_path)
    plt.close()

def plot_memory_usage(memory_data, output_path):
# memory piechart
    labels = ['Used Memory', 'Available Memory']
    sizes = [memory_data['used'], memory_data['available']]

    plt.figure(figsize=(6, 6))
    plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140)
    plt.axis('equal')
    plt.title('Memory Usage Breakdown')
    plt.savefig(output_path)
    plt.close()

def plot_cpu_usage(cpu_usage, output_path):
    #cpu bar
    plt.figure(figsize=(8, 4))
    plt.barh(['CPU Usage'], [cpu_usage], color='blue')
    plt.xlim(0, 100)
    plt.xlabel('Percentage (%)')
    plt.title('Current CPU Usage')
    plt.savefig(output_path)
    plt.close()


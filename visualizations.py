import matplotlib.pyplot as plt

def plot_disk_usage(disk_data):
    """Creates a pie chart for disk usage data."""
    labels = ['Free Space', 'Used Space']
    sizes = [disk_data['Free Space'], disk_data['Used Space']]

    plt.figure(figsize=(6, 6))
    plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140)
    plt.axis('equal')
    plt.title('Disk Usage Breakdown')
    plt.show()

def plot_memory_usage(memory_data):
    """Creates a pie chart for memory usage data."""
    labels = ['Used Memory', 'Available Memory']
    sizes = [memory_data['used'], memory_data['available']]

    plt.figure(figsize=(6, 6))
    plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140)
    plt.axis('equal')
    plt.title('Memory Usage Breakdown')
    plt.show()

def plot_cpu_usage(cpu_usage):
    """Creates a gauge-like bar plot to represent CPU usage."""
    plt.figure(figsize=(8, 4))
    plt.barh(['CPU Usage'], [cpu_usage], color='blue')
    plt.xlim(0, 100)  # Assuming CPU usage is a percentage value (0-100)
    plt.xlabel('Percentage (%)')
    plt.title('Current CPU Usage')
    plt.show()

# Example usage
if __name__ == "__main__":
    # Example data
    example_disk_data = {
        'Free Space': 743525101568,
        'Used Space': 10244407296
    }

    example_memory_data = {
        'used': 16451059712,
        'available': 17034035200
    }

    example_cpu_usage = 11.8

    # Call visualizations
    plot_disk_usage(example_disk_data)
    plot_memory_usage(example_memory_data)
    plot_cpu_usage(example_cpu_usage)

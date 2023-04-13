from batsim_py import SimulatorHandler
from scheduler.fcfs import FCFSScheduler

if __name__ == "__main__":
    workloads_path = "workloads/fcfs.json"
    platform_path = "platform/platform-8-host.xml"
    simulator = SimulatorHandler()
    simulator.start(platform=platform_path, workload=workloads_path)
    scheduler = FCFSScheduler(simulator)
    while simulator.is_running:
        print("+++++ TIME:", simulator.current_time)
        print("QUEUE before assignment:",simulator.queue)
        scheduler.schedule()
        print("QUEUE after assignment:",simulator.queue)
        print("KEADAAN HOST:\n-----------------------")
        for host in simulator.platform.hosts:
            print(host,host.jobs)
        print("-----------------------")
        simulator.proceed_time(10)
    simulator.close()
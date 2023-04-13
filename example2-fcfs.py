from batsim_py import SimulatorHandler
from fcfs import FCFSScheduler

if __name__ == "__main__":
    workloads_path = "workloads/simple-8-host.json"
    platform_path = "platform/platform-8-host.xml"
    simulator = SimulatorHandler()
    simulator.start(platform=platform_path, workload=workloads_path)
    scheduler = FCFSScheduler(simulator)
    while simulator.is_running:
        print("QUEUE before assignment:",simulator.queue)
        scheduler.schedule()
        print("QUEUE after assignment:",simulator.queue)
        simulator.proceed_time(10)
    simulator.close()
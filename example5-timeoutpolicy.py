from batsim_py import SimulatorHandler
from scheduler.easy_backfilling import EASYScheduler
from power_policy.timeout_policy import TimeoutPolicy

if __name__ == "__main__":
    workloads_path = "workloads/easybf.json"
    platform_path = "platform/platform-8-host.xml"
    simulator = SimulatorHandler()
    simulator.start(platform=platform_path, workload=workloads_path)
    scheduler = EASYScheduler(simulator)
    pw_policy = TimeoutPolicy(5, simulator)
    while simulator.is_running:
        print("+++++ TIME:", simulator.current_time)
        print("QUEUE before assignment:",simulator.queue)
        scheduler.schedule()
        print("QUEUE after assignment:",simulator.queue)
        print("KEADAAN HOST:\n-----------------------")
        for host in simulator.platform.hosts:
            print(host,host.jobs)
        print("-----------------------")
        simulator.proceed_time(5)  
    simulator.close()
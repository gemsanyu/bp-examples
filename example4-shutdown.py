from batsim_py import SimulatorHandler
from scheduler.easy_backfilling import EASYScheduler


def shutdown_last_two(simulator:SimulatorHandler):
    simulator.switch_off([6,7])

if __name__ == "__main__":
    workloads_path = "workloads/easybf.json"
    platform_path = "platform/platform-8-host.xml"
    simulator = SimulatorHandler()
    simulator.start(platform=platform_path, workload=workloads_path)
    scheduler = EASYScheduler(simulator)
    shutdown_t = 30
    while simulator.is_running:
        if simulator.current_time == shutdown_t:
            shutdown_last_two(simulator)
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

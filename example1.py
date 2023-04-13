from batsim_py import SimulatorHandler


if __name__ == "__main__":
    workloads_path = "workloads/simple-8-host.json"
    platform_path = "platform/platform-8-host.xml"
    simulator = SimulatorHandler()
    simulator.start(platform=platform_path, workload=workloads_path)
    while not simulator.is_submitter_finished:
        simulator.proceed_time(10)
        print(simulator.queue)
    simulator.close()
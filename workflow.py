from toil.common import Toil
from toil.job import Job

def helloWorld(job, message, memory="1G", cores=1, disk="1G"):
    job.log(f"Hello, world! {message}")

if __name__ == "__main__":
    parser = Job.Runner.getDefaultArgumentParser()
    options = parser.parse_args()
    options.clean = "always"

    parent_job = Job.wrapJobFn(helloWorld, "FIRST JOB")

    for i in range(0, 10):
        parent_job.addChildJobFn(helloWorld, i)

    with Toil(options) as toil:
        if not workflow.options.restart:
            toil.start(parent_job)
        else:
            sortedFileID = workflow.restart()

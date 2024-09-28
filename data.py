import pandas


class Data:

    def __init__(self, job_title: list, job_description: list, job_payment: list, job_link: list, topic):
        self.job_dict = {
            "Job Title": job_title,
            "Job Description": job_description,
            "Job Payment": job_payment,
            "Job Link": job_link

        }

        self.topic = topic

    def crate_cvs(self):
        dataframe = pandas.DataFrame.from_dict(self.job_dict)
        dataframe.to_csv(f'output/jobs_for_{self.topic}.csv', sep=';', index=False)

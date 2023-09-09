import json

from matching import get_recommended_job_for_member
from models import Job, Member


def main():
    with open('./members.json') as f:
        members = [Member(**member) for member in json.load(f)]

    with open('./jobs.json') as f:
        jobs = [Job(**job) for job in json.load(f)]

    for member in members:
        job = get_recommended_job_for_member(member, jobs)
        print('Perfect job for member "{}": {}'.format(member.name, job))


if __name__ == '__main__':
    main()

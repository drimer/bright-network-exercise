from models import Member, Job


def get_location_score(member: Member, job: Job) -> int:
    score = 0
    member_bio = member.bio.lower()
    job_location = job.location.lower()

    if 'outside of {}'.format(job_location) in member_bio:
        score -= 1
    elif 'relocate to {}'.format(job_location) in member_bio:
        score += 1
    elif job.location.lower() in member_bio:
        score += 1

    return score


def get_similarity_score(member: Member, job: Job) -> int:
    score = 0
    member_bio = member.bio.lower()
    job_title = job.title.lower()

    for word in job_title.split():  # Terrible!! This isn't good enough to extract words from string
        if word in member_bio:
            score += 1

    score += get_location_score(member, job)

    return score


def get_recommended_job_for_member(member: Member, all_jobs: list[Job]) -> Job:
    jobs_and_scores = []
    for job in all_jobs:
        score = get_similarity_score(member, job)
        jobs_and_scores.append((job, score))

    return max(jobs_and_scores, key=lambda js: js[1])[0]

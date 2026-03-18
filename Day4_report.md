# Day 4 Report — Labs 6–7 (Docker + Jenkins + Security + Ansible)

## 1) Student
- Name: Massalimov Ilyas
- Group: IB-23-5b
- Token: D1-IB-23-5b-11-7A51
- Repo: https://github.com/zxcsalam/devnet-day1-IB_23_5b-massalimov

## 2) Evidence checklist (files exist)
### Docker (6.2.7)
- artifacts/day4/docker/sampleapp_curl.txt: [Yes]
- artifacts/day4/docker/sampleapp_token_proof.txt: [Yes]
- artifacts/day4/docker/sampleapp_docker_ps.txt: [Yes]
- artifacts/day4/docker/sampleapp_build_log.txt: [Yes]

### Jenkins (6.3.6)
- artifacts/day4/jenkins/jenkins_docker_ps.txt: [Yes]
- artifacts/day4/jenkins/buildapp_console.txt: [Yes]
- artifacts/day4/jenkins/testapp_console.txt: [Yes]
- artifacts/day4/jenkins/pipeline_script.groovy: [Yes]
- artifacts/day4/jenkins/pipeline_console.txt: [Yes]
- artifacts/day4/jenkins/jenkins_url.txt: [Yes]

### Ansible (7.4.8)
- artifacts/day4/ansible/ansible_ping.txt: [Yes]
- artifacts/day4/ansible/ansible_hello.txt: [Yes]
- artifacts/day4/ansible/ansible_playbook_install.txt: [Yes]
- artifacts/day4/ansible/ports_conf_after.txt: [Yes]
- artifacts/day4/ansible/curl_apache_8081.txt: [Yes]

### Security (6.5.10)
- artifacts/day4/security/signup_v1.txt: [Yes]
- artifacts/day4/security/login_v1.txt: [Yes]
- artifacts/day4/security/signup_v2.txt: [Yes]
- artifacts/day4/security/login_v2.txt: [Yes]
- artifacts/day4/security/db_tables.txt: [Yes]
- artifacts/day4/security/db_user_hash_sample.txt: [Yes]

## 3) Commands output

### 3.1) Summary
```text
{
  "schema_version": "4.1",
  "generated_utc": "2026-03-18T16:34:47.261911+00:00",
  "student": {
    "token": "D1-IB-23-5b-11-7A51",
    "token_hash8": "8621b72d",
    "name": "Massalimov-Ilyas",
    "group": "IB-23-5b"
  },
  "checks": {
    "docker_token_in_page": true,
    "docker_tokenproof": true,
    "ansible_port_8081": true,
    "jenkins_pipeline_has_stages": true,
    "security_db_has_tables": true
  },
  "evidence_sha256": {
    "docker_sampleapp_curl": "19e14bcd20ae44858b8916882cd7ea77060649168504b0e60d5adca0eb8358df",
    "docker_ps": "94e051a3977260b6021fbd9adc9c8f1be8c7c3e4a7c0e2749d8c6e0d4930070f",
    "docker_build_log": "089e6ade3352ac357c4f7143ab6e0a7307f7e782597e54884a01980b3d35d70c",
    "docker_token_proof": "07fe5e8d6ae45a299b088460df9bbb4725d43cbcc2aabf6b2ef8412fa9a07d3d",
    "jenkins_docker_ps": "02400e34c7ebfd4b200231a7e58cae670b5a8b1efeaf37a5b6fd0f397475f8b0",
    "buildapp_console": "f264fc78b77e634aa90e711282fef4eac737f2cf86d628d0554cc8150a6893cc",
    "testapp_console": "fe801cd64a0ee48c7cff303275edee2b52b5db9c1d8566a9145e7f227f1350b0",
    "pipeline_script": "5f768e5c3327f239d4d596b619d3bb7327148137db26778e5c83bced278c77ef",
    "pipeline_console": "8e5d283996b14a47ddff80e74c87129a15b256263f3663c5aaa5a88d13e6d1f6",
    "jenkins_url": "387db443878e39df26fe9826db1fd40100b146f93795b07fda3bfeef709b5aca",
    "ansible_ping": "005e9245df2c530d64aee6bfec751dfc3ced4b06361f597e7fde4163bc44fd69",
    "ansible_hello": "6b506fcd95eb0febede6e36542f9524299ecd459f7b11b6743bef44138cbb0fb",
    "ansible_playbook_install": "f714e4d11c930a147edb611c6721568a94d957a8e1db7b304ce05ddc00cfcf1e",
    "ports_conf_after": "8ee0ac8272eaa90ca6a9597cb472034768331e543d074cc72141b520ffb6f686",
    "curl_apache_8081": "e870932d034a48187d6685a82452e2dfbd36db1ae9840a89275eaab07b73a009",
    "signup_v1": "d299da4792553b50de72449cda41e26da947f741018a6c11f3a94b009be6579f",
    "login_v1": "4e885c0fa26fb9497717e18e8a289a45d1cce748c0bd91a401302c729ca48cfc",
    "signup_v2": "d299da4792553b50de72449cda41e26da947f741018a6c11f3a94b009be6579f",
    "login_v2": "4e885c0fa26fb9497717e18e8a289a45d1cce748c0bd91a401302c729ca48cfc",
    "db_tables": "93dea430def06bb6214d5e2ce362ea0f455d07af66385629b2a36ab40ea6d654",
    "db_user_hash_sample": "21aa0b040100127b08679ce94f1733a3d712c2674e96f5a5031b1474bbe58965"
  },
  "validation_passed": true,
  "run": {
    "python": "3.8.2",
    "platform": "linux"
  }
}
```

### 3.2) Pytest
``` text
(.venv) devasc@labvm:~/devnet-day1-MIS$ pytest -q
....                                           [100%]
4 passed in 0.79s
```
## 4) Short reflection (5–8 lines)
- What was the hardest part today and why?

Работа в Jenkins, интерфейс очень сырой и почти ничего не понятно, но разобрался в этом


- One security mistake you avoided (or made and fixed):

Изначальное хранение паролей в USER_PLAIN, которое было исправлено переходом на USER_HASH с SHA-256.

## 5) Problems & fixes (at least 1)
- Problem:

При запуске ansible ping возникла ошибка: [WARNING]: Ansible is being run in a world writable directory. Ansible игнорировал файл конфигурации ansible.cfg, потому что папка проекта имела слишком свободные права доступа (777), что небезопасно.

- Fix:

Принудительно указали путь к конфигу через переменную окружения export ANSIBLE_CONFIG=....

- Proof:

Файл ansible_ping.txt содержит статус SUCCESS и pong.

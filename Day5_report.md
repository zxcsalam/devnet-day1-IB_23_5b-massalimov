# Day 5 Report — Module 8 Capstone

## 1) Student
- Name: Massalimov Ilyas
- Group: IB-23-5b
- Token: D1-IB-23-5b-11-7A51
- Repo: https://github.com/zxcsalam/devnet-day1-IB_23_5b-massalimov

## 2) YANG (8.3.5)
- Evidence files:
  - artifacts/day5/yang/ietf-interfaces.yang: [Yes]
  - artifacts/day5/yang/pyang_version.txt: [Yes]
  - artifacts/day5/yang/pyang_tree.txt: [Yes]

## 3) Webex (8.6.7)
- Room title contains token_hash8: [Yes]
- Message text contains token_hash8: [Yes]
- Evidence files:
  - me.json / rooms_list.json / room_create.json / message_post.json / messages_list.json: [Yes]

## 4) Packet Tracer Controller REST (8.8.3)
- external_access_check contains “empty ticket”: [Yes]
- serviceTicket saved: [Yes]
- Evidence files:
  - external_access_check.json / network_devices.json / hosts.json: [Yes]
  - postman_collection.json / postman_environment.json: [Yes]
  - pt_internal_output.txt: [Yes]

## 5) Commands output (paste exact)

### 5.1) Summary
```text
{
  "schema_version": "5.0",
  "generated_utc": "2026-03-19T15:19:47.593849+00:00",
  "student": {
    "token": "D1-IB-23-5b-11-7A51",
    "token_hash8": "8621b72d",
    "name": "Massalimov-Ilyas",
    "group": "IB-23-5b"
  },
  "yang": {
    "ok": true,
    "evidence_sha": "949de5d3ee156508fe0af9f6a93bb6b16cf3e397ba9f6ba226e1c50bb5256edb"
  },
  "webex": {
    "ok": true,
    "room_title_contains_hash8": true,
    "evidence_sha": "9f963f94f8f65dd4853ae39326fe4d1c91ca084d31e7a98e230453d610da9d55"
  },
  "pt": {
    "ok": true,
    "empty_ticket_seen": true,
    "evidence_sha": "7a06bc666b72015739df299f81f0ba6a2d7fc59bf21dcedfd3b3de0b7a1b1042"
  },
  "validation_passed": true,
  "run": {
    "python": "3.8.2",
    "platform": "linux"
  }
}
```

### 5.2) Pytest

```text
(.venv) devasc@labvm:~/devnet-day1-MIS$ pytest -q
.....                                               [100%]
5 passed in 1.07s
```

## 6) Problems & fixes (at least 1)
- Problem:

При открытии вкладки Programming в Network Controller внутри Packet Tracer страница оставалась белой или не прогружалась, что не позволяло включить доступ к API.

- Fix:

Открыл файл Packet Tracer на самой системе, не на машине

- Proof:

Смог выполнить скрипт в который записал в pt_internal_output.txt
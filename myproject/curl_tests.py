

curl -X POST -d "username=anuragmadde&password=1234" http://127.0.0.1:8000/api/token/auth/

curl -X POST -H "Authorization: JWT eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoyLCJ1c2VybmFtZSI6ImFudXJhZ21hZGRlIiwiZW1haWwiOiJhbnVyYWdtYWRkZUBob3RtYWlsLmNvbSIsImV4cCI6MTQ3MDc2NTMzNn0.JBf0VDbjv_gnnDUqqKwZvHsar0diG4DSMsP_h_GK2wU" -H "Content-Type: application/json" -d "content=Comment from curl" "http://127.0.0.1:8000/api/comments/create/?type=blog&slug=new-post"
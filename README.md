# appsignal-samples

Generate CSV of Appsignal project samples

## Command
```
python3 main.py "app-id" "personal-api-token" "sample-type" "&action_id=App::V1::XYZController-hash-method&limit=25&since=1606463290" "file-name"
```

## Arguments

```
app-id: Application ID
personal-api-token: Under Profile & Settings of Appsignal dashboard
sample-type: performance OR errors
```

For More Info, read [AppSignal API docs](https://docs.appsignal.com/api/samples.html)
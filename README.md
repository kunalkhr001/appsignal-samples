# appsignal-samples

Generate CSV of Appsignal project samples

## Command
```
python3 main.py "app-id" "personal-api-token" "sample-type" "&action_id=App::V1::XYZController-hash-method&limit=25&since=1606463290&before=1606464445" "file-name"
```

## Arguments

```
app-id: Application ID
personal-api-token: Under Profile & Settings of Appsignal dashboard
sample-type: performance OR errors
action_id, limit, since, before: These are some of the query params, you can find more of these & their usage in the api docs
```

For More Info, read [AppSignal API docs](https://docs.appsignal.com/api/samples.html)
# Flask app

## development

### Flask api

```sh
$ cd api
$ cp .env.example .env
$ pip3 install --upgrade -r requirements.txt
$ python3 app.py
...
INFO:werkzeug: * Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
```

#### :whale: Run docker :ocean:
```sh
$ docker-compose build
$ docker-compose up
Attaching to flask_api
```

access `localhost:5000`

## :surfer::ocean: API

返されるデータ
```typescript
[
  story_no: int;
  title: string;
  // ...
  {
    op?: string;
    ed?: string;
  },
  date: string;
]
```

### `/api/random`

ランダムにデータを1つ返します

**Return**
```js
{
  'status': 'ok',
  'data': [...]
}
```

### `/api/stories/<int:story_no>`

`story_no` に該当する話数のデータを返します  
該当する話数が無い場合は `null` を返します

**Return**
```js
{
  'status': 'ok',
  'data': [...]
}
```

### `/api/search?keyword=<keyword>`

`keyword` にマッチする話数のリストを返します  
該当する話数が無い場合は `[]` から配列を返します

**Return**
```js
{
  'status': 'ok',
  'data': [
    [...]
    // ...
  ]
}
```

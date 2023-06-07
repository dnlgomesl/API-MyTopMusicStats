
# API - My Top Músic Stats
*URL* = https://18.191.97.102.nip.io

O My Top Music Stats é um projeto de Trabalho de Conclusão de Curso que visa mostrar para você que usa o Spotify um pequeno dashboard com informações referente ao que você vem escutando.

## Endpoints da API
A seguir, estão listados os endpoints disponíveis na API:

### 1. Endpoint de Status

Endpoint: GET /status/

Esse endpoint retorna o status da api.

Exemplo de resposta:

```json
{
	"status": "online",
	"timestamp": 1686165804,
	"started": 1684972097,
	"service": "api-tcc",
	"version": "1.1"
}

```

### 2. Artists

Endpoint: POST /artists/

Esse endpoint retorna a listagem do artistas mais ouvidos no intervalo de tempo definido pelo parâmetro `range`, a quantidade definida pelo parâmetro `limit`e a ordenação pelo parâmetro `sort`. Por fim ele recebe um `token` referente ao login com o Spotify.

#### Exemplo de payload

```json
{
    "token": "<auth_token>",
    "range": "medium_term",
    "limit": "20",
		"sort": "popularity"
}
```

Os valores possíveis para `range` são `medium_term`, `short_term` e `long_term`. 
Os valores possíveis para `sort` são `popularity`, `duration` e `padrao`.
Os valores possíveis para `limit` vão de 1 a 50.

#### Exemplo de resposta:

```json
{
	"top": [
		{
			"artist": "Dream Theater",
			"genres": [
				"hard rock",
				"metal",
				"progressive metal"
			],
			"images": [
				{
					"height": 640,
					"url": "https://i.scdn.co/image/ab6761610000e5eb881f3d1db94c120edca60a65",
					"width": 640
				},
				{
					"height": 320,
					"url": "https://i.scdn.co/image/ab67616100005174881f3d1db94c120edca60a65",
					"width": 320
				},
				{
					"height": 160,
					"url": "https://i.scdn.co/image/ab6761610000f178881f3d1db94c120edca60a65",
					"width": 160
				}
			],
			"popularity": 60,
			"url": "https://open.spotify.com/artist/2aaLAng2L2aWD2FClzwiep"
		},
		{
			"artist": "John Mayer",
			"genres": [
				"neo mellow",
				"singer-songwriter"
			],
			"images": [
				{
					"height": 640,
					"url": "https://i.scdn.co/image/ab6761610000e5ebe926dd683e1700a6d65bd835",
					"width": 640
				},
				{
					"height": 320,
					"url": "https://i.scdn.co/image/ab67616100005174e926dd683e1700a6d65bd835",
					"width": 320
				},
				{
					"height": 160,
					"url": "https://i.scdn.co/image/ab6761610000f178e926dd683e1700a6d65bd835",
					"width": 160
				}
			],
			"popularity": 77,
			"url": "https://open.spotify.com/artist/0hEurMDQu99nJRq8pTxO14"
		},
		{
			"artist": "Duzz",
			"genres": [
				"brazilian hip hop"
			],
			"images": [
				{
					"height": 640,
					"url": "https://i.scdn.co/image/ab6761610000e5eb80859167b16b515cfc181f27",
					"width": 640
				},
				{
					"height": 320,
					"url": "https://i.scdn.co/image/ab6761610000517480859167b16b515cfc181f27",
					"width": 320
				},
				{
					"height": 160,
					"url": "https://i.scdn.co/image/ab6761610000f17880859167b16b515cfc181f27",
					"width": 160
				}
			],
			"popularity": 56,
			"url": "https://open.spotify.com/artist/4oPnjkJcLqOim9KJxvIYMz"
		},
		{
			"artist": "Rodolfo Abrantes",
			"genres": [
				"adoracao",
				"brazilian gospel",
				"rock gospel brasileiro"
			],
			"images": [
				{
					"height": 640,
					"url": "https://i.scdn.co/image/ab6761610000e5ebe3373f879acf46f60aff941e",
					"width": 640
				},
				{
					"height": 320,
					"url": "https://i.scdn.co/image/ab67616100005174e3373f879acf46f60aff941e",
					"width": 320
				},
				{
					"height": 160,
					"url": "https://i.scdn.co/image/ab6761610000f178e3373f879acf46f60aff941e",
					"width": 160
				}
			],
			"popularity": 51,
			"url": "https://open.spotify.com/artist/0M8rmgpYMtvYbHvXD3cHkN"
		},
		{
			"artist": "UCLÃ",
			"genres": [
				"trap brasileiro"
			],
			"images": [
				{
					"height": 640,
					"url": "https://i.scdn.co/image/ab6761610000e5ebc61a6486789a3b93226e03b7",
					"width": 640
				},
				{
					"height": 320,
					"url": "https://i.scdn.co/image/ab67616100005174c61a6486789a3b93226e03b7",
					"width": 320
				},
				{
					"height": 160,
					"url": "https://i.scdn.co/image/ab6761610000f178c61a6486789a3b93226e03b7",
					"width": 160
				}
			],
			"popularity": 57,
			"url": "https://open.spotify.com/artist/4zP89WNloauEX8v8JdZbxP"
		},
		{
			"artist": "NX Zero",
			"genres": [
				"brazilian emo",
				"brazilian rock",
				"pop rock brasileiro",
				"rock alternativo brasileiro"
			],
			"images": [
				{
					"height": 640,
					"url": "https://i.scdn.co/image/ab6761610000e5eb9f26cb33eabb598942820a7b",
					"width": 640
				},
				{
					"height": 320,
					"url": "https://i.scdn.co/image/ab676161000051749f26cb33eabb598942820a7b",
					"width": 320
				},
				{
					"height": 160,
					"url": "https://i.scdn.co/image/ab6761610000f1789f26cb33eabb598942820a7b",
					"width": 160
				}
			],
			"popularity": 59,
			"url": "https://open.spotify.com/artist/1A3dFCPF68vh5lyxzBqLUH"
		},
		{
			"artist": "Marco Telles",
			"genres": [
				"adoracao",
				"indie cristao"
			],
			"images": [
				{
					"height": 640,
					"url": "https://i.scdn.co/image/ab6761610000e5eb1ecd0c98c145ed25dcfefac1",
					"width": 640
				},
				{
					"height": 320,
					"url": "https://i.scdn.co/image/ab676161000051741ecd0c98c145ed25dcfefac1",
					"width": 320
				},
				{
					"height": 160,
					"url": "https://i.scdn.co/image/ab6761610000f1781ecd0c98c145ed25dcfefac1",
					"width": 160
				}
			],
			"popularity": 48,
			"url": "https://open.spotify.com/artist/1i2hM139lmyTdukYTJKHsJ"
		},
		{
			"artist": "Slipknot",
			"genres": [
				"alternative metal",
				"nu metal",
				"rap metal",
				"rock"
			],
			"images": [
				{
					"height": 640,
					"url": "https://i.scdn.co/image/ab6761610000e5ebec01c52d6030a1574070e308",
					"width": 640
				},
				{
					"height": 320,
					"url": "https://i.scdn.co/image/ab67616100005174ec01c52d6030a1574070e308",
					"width": 320
				},
				{
					"height": 160,
					"url": "https://i.scdn.co/image/ab6761610000f178ec01c52d6030a1574070e308",
					"width": 160
				}
			],
			"popularity": 78,
			"url": "https://open.spotify.com/artist/05fG473iIaoy82BF1aGhL8"
		},
		{
			"artist": "Graça",
			"genres": [
				"indie cristao"
			],
			"images": [
				{
					"height": 640,
					"url": "https://i.scdn.co/image/ab6761610000e5eb756e197ee27680603a77c99c",
					"width": 640
				},
				{
					"height": 320,
					"url": "https://i.scdn.co/image/ab67616100005174756e197ee27680603a77c99c",
					"width": 320
				},
				{
					"height": 160,
					"url": "https://i.scdn.co/image/ab6761610000f178756e197ee27680603a77c99c",
					"width": 160
				}
			],
			"popularity": 5,
			"url": "https://open.spotify.com/artist/1o3Q4qUzpBESVzQvWHaRpd"
		},
		{
			"artist": "CantoVerbo",
			"genres": [
				"adoracao"
			],
			"images": [
				{
					"height": 640,
					"url": "https://i.scdn.co/image/ab6761610000e5eb71540892bc8b2c3e9a091561",
					"width": 640
				},
				{
					"height": 320,
					"url": "https://i.scdn.co/image/ab6761610000517471540892bc8b2c3e9a091561",
					"width": 320
				},
				{
					"height": 160,
					"url": "https://i.scdn.co/image/ab6761610000f17871540892bc8b2c3e9a091561",
					"width": 160
				}
			],
			"popularity": 33,
			"url": "https://open.spotify.com/artist/33zJpM6XSs9wr7oj46660Z"
		},
		{
			"artist": "Oficina G3",
			"genres": [
				"adoracao",
				"brazilian gospel",
				"brazilian metal",
				"brazilian progressive metal",
				"rock gospel brasileiro"
			],
			"images": [
				{
					"height": 640,
					"url": "https://i.scdn.co/image/ab6761610000e5eba4ab8b2114b45b414c453a4e",
					"width": 640
				},
				{
					"height": 320,
					"url": "https://i.scdn.co/image/ab67616100005174a4ab8b2114b45b414c453a4e",
					"width": 320
				},
				{
					"height": 160,
					"url": "https://i.scdn.co/image/ab6761610000f178a4ab8b2114b45b414c453a4e",
					"width": 160
				}
			],
			"popularity": 50,
			"url": "https://open.spotify.com/artist/0gO5Vbklho8yrBrUdHhuLH"
		},
		{
			"artist": "Krawk",
			"genres": [
				"trap brasileiro"
			],
			"images": [
				{
					"height": 640,
					"url": "https://i.scdn.co/image/ab6761610000e5eb2fc0a3ebac4d21de553437ca",
					"width": 640
				},
				{
					"height": 320,
					"url": "https://i.scdn.co/image/ab676161000051742fc0a3ebac4d21de553437ca",
					"width": 320
				},
				{
					"height": 160,
					"url": "https://i.scdn.co/image/ab6761610000f1782fc0a3ebac4d21de553437ca",
					"width": 160
				}
			],
			"popularity": 50,
			"url": "https://open.spotify.com/artist/7a99I3BHPvsv4aBVNqb4g4"
		},
		{
			"artist": "Stone Sour",
			"genres": [
				"alternative metal",
				"nu metal",
				"post-grunge",
				"rock"
			],
			"images": [
				{
					"height": 640,
					"url": "https://i.scdn.co/image/ab6761610000e5ebf4c48660e778eeea3d9f1c5b",
					"width": 640
				},
				{
					"height": 320,
					"url": "https://i.scdn.co/image/ab67616100005174f4c48660e778eeea3d9f1c5b",
					"width": 320
				},
				{
					"height": 160,
					"url": "https://i.scdn.co/image/ab6761610000f178f4c48660e778eeea3d9f1c5b",
					"width": 160
				}
			],
			"popularity": 63,
			"url": "https://open.spotify.com/artist/49qiE8dj4JuNdpYGRPdKbF"
		},
		{
			"artist": "Metallica",
			"genres": [
				"hard rock",
				"metal",
				"old school thrash",
				"rock",
				"thrash metal"
			],
			"images": [
				{
					"height": 640,
					"url": "https://i.scdn.co/image/ab6761610000e5eb69ca98dd3083f1082d740e44",
					"width": 640
				},
				{
					"height": 320,
					"url": "https://i.scdn.co/image/ab6761610000517469ca98dd3083f1082d740e44",
					"width": 320
				},
				{
					"height": 160,
					"url": "https://i.scdn.co/image/ab6761610000f17869ca98dd3083f1082d740e44",
					"width": 160
				}
			],
			"popularity": 82,
			"url": "https://open.spotify.com/artist/2ye2Wgw4gimLv2eAKyk1NB"
		},
		{
			"artist": "Menestrel",
			"genres": [
				"brazilian hip hop",
				"rap df"
			],
			"images": [
				{
					"height": 640,
					"url": "https://i.scdn.co/image/ab6761610000e5eb4b167368cc15eeb69fa11ddb",
					"width": 640
				},
				{
					"height": 320,
					"url": "https://i.scdn.co/image/ab676161000051744b167368cc15eeb69fa11ddb",
					"width": 320
				},
				{
					"height": 160,
					"url": "https://i.scdn.co/image/ab6761610000f1784b167368cc15eeb69fa11ddb",
					"width": 160
				}
			],
			"popularity": 48,
			"url": "https://open.spotify.com/artist/4eQ4RMjplRznwHA1UBNnXT"
		},
		{
			"artist": "Linkin Park",
			"genres": [
				"alternative metal",
				"nu metal",
				"post-grunge",
				"rap metal",
				"rock"
			],
			"images": [
				{
					"height": 640,
					"url": "https://i.scdn.co/image/ab6761610000e5eb811da3b2e7c9e5a9c1a6c4f7",
					"width": 640
				},
				{
					"height": 320,
					"url": "https://i.scdn.co/image/ab67616100005174811da3b2e7c9e5a9c1a6c4f7",
					"width": 320
				},
				{
					"height": 160,
					"url": "https://i.scdn.co/image/ab6761610000f178811da3b2e7c9e5a9c1a6c4f7",
					"width": 160
				}
			],
			"popularity": 85,
			"url": "https://open.spotify.com/artist/6XyY86QOPPrYVGvF9ch6wz"
		},
		{
			"artist": "Dani Black",
			"genres": [
				"nova mpb"
			],
			"images": [
				{
					"height": 640,
					"url": "https://i.scdn.co/image/ab6761610000e5eb943d1a5498f6b9584e4cc777",
					"width": 640
				},
				{
					"height": 320,
					"url": "https://i.scdn.co/image/ab67616100005174943d1a5498f6b9584e4cc777",
					"width": 320
				},
				{
					"height": 160,
					"url": "https://i.scdn.co/image/ab6761610000f178943d1a5498f6b9584e4cc777",
					"width": 160
				}
			],
			"popularity": 34,
			"url": "https://open.spotify.com/artist/5DlaVYlcVjPYeC4QLZDBJa"
		},
		{
			"artist": "Projeto Sola",
			"genres": [
				"musica crista reformada"
			],
			"images": [
				{
					"height": 640,
					"url": "https://i.scdn.co/image/ab6761610000e5eb7813e9e788bacc2992d340be",
					"width": 640
				},
				{
					"height": 320,
					"url": "https://i.scdn.co/image/ab676161000051747813e9e788bacc2992d340be",
					"width": 320
				},
				{
					"height": 160,
					"url": "https://i.scdn.co/image/ab6761610000f1787813e9e788bacc2992d340be",
					"width": 160
				}
			],
			"popularity": 50,
			"url": "https://open.spotify.com/artist/7frHe3lyyKF5Uo1rDZ058K"
		},
		{
			"artist": "Travis Scott",
			"genres": [
				"hip hop",
				"rap",
				"slap house"
			],
			"images": [
				{
					"height": 640,
					"url": "https://i.scdn.co/image/ab6761610000e5ebe707b87e3f65997f6c09bfff",
					"width": 640
				},
				{
					"height": 320,
					"url": "https://i.scdn.co/image/ab67616100005174e707b87e3f65997f6c09bfff",
					"width": 320
				},
				{
					"height": 160,
					"url": "https://i.scdn.co/image/ab6761610000f178e707b87e3f65997f6c09bfff",
					"width": 160
				}
			],
			"popularity": 89,
			"url": "https://open.spotify.com/artist/0Y5tJX1MQlPlqiwlOH1tJY"
		},
		{
			"artist": "L7NNON",
			"genres": [
				"funk rj",
				"pop rap brasileiro",
				"trap brasileiro"
			],
			"images": [
				{
					"height": 640,
					"url": "https://i.scdn.co/image/ab6761610000e5eb15d5eb35b531d18fc96f4c26",
					"width": 640
				},
				{
					"height": 320,
					"url": "https://i.scdn.co/image/ab6761610000517415d5eb35b531d18fc96f4c26",
					"width": 320
				},
				{
					"height": 160,
					"url": "https://i.scdn.co/image/ab6761610000f17815d5eb35b531d18fc96f4c26",
					"width": 160
				}
			],
			"popularity": 75,
			"url": "https://open.spotify.com/artist/0JjPiLQNgAFaEkwoy56B1C"
		}
	],
	"additional": {
		"genres": {
			"adoracao": 4,
			"rock": 4,
			"trap brasileiro": 3,
			"alternative metal": 3,
			"nu metal": 3,
			"hard rock": 2,
			"metal": 2,
			"brazilian hip hop": 2,
			"brazilian gospel": 2,
			"rock gospel brasileiro": 2,
			"indie cristao": 2,
			"rap metal": 2,
			"post-grunge": 2,
			"progressive metal": 1,
			"neo mellow": 1,
			"singer-songwriter": 1,
			"brazilian emo": 1,
			"brazilian rock": 1,
			"pop rock brasileiro": 1,
			"rock alternativo brasileiro": 1,
			"brazilian metal": 1,
			"brazilian progressive metal": 1,
			"old school thrash": 1,
			"thrash metal": 1,
			"rap df": 1,
			"nova mpb": 1,
			"musica crista reformada": 1,
			"hip hop": 1,
			"rap": 1,
			"slap house": 1,
			"funk rj": 1,
			"pop rap brasileiro": 1
		},
		"popularity": {
			"mean": 57.5,
			"mode": 50,
			"median": 56.5
		}
	}
}
```
### 3. Tracks

Endpoint: POST /tracks/

Esse endpoint retorna a listagem das músicas mais ouvidas no intervalo de tempo definido pelo parâmetro `range`, a quantidade definida pelo parâmetro `limit`e a ordenação pelo parâmetro `sort`. Por fim ele recebe um `token` referente ao login com o Spotify.

#### Exemplo de payload

```json
{
    "token": "<auth_token>",
    "range": "long_term",
    "limit": "20",
		"sort": "duration"
}
```

Os valores possíveis para `range` são `medium_term`, `short_term` e `long_term`. 
Os valores possíveis para `sort` são `popularity`, `duration` e `padrao`.
Os valores possíveis para `limit` vão de 1 a 50.

#### Exemplo de resposta:

```json
{
	"top": [
		{
			"music": "The Best of Times",
			"artist": "Dream Theater",
			"album": "Black Clouds & Silver Linings",
			"images": [
				{
					"height": 640,
					"url": "https://i.scdn.co/image/ab67616d0000b2735fa53cb7507e4c55178ead5a",
					"width": 640
				},
				{
					"height": 300,
					"url": "https://i.scdn.co/image/ab67616d00001e025fa53cb7507e4c55178ead5a",
					"width": 300
				},
				{
					"height": 64,
					"url": "https://i.scdn.co/image/ab67616d000048515fa53cb7507e4c55178ead5a",
					"width": 64
				}
			],
			"popularity": 41,
			"date": "2009-06-19",
			"duration": 13.7,
			"url": "https://open.spotify.com/track/0yo6lVHmhSRLW0dWopkcRv",
			"id": "0yo6lVHmhSRLW0dWopkcRv"
		},
		{
			"music": "This Is the Life",
			"artist": "Dream Theater",
			"album": "A Dramatic Turn of Events",
			"images": [
				{
					"height": 640,
					"url": "https://i.scdn.co/image/ab67616d0000b27331c73a24eff2186e4abe070d",
					"width": 640
				},
				{
					"height": 300,
					"url": "https://i.scdn.co/image/ab67616d00001e0231c73a24eff2186e4abe070d",
					"width": 300
				},
				{
					"height": 64,
					"url": "https://i.scdn.co/image/ab67616d0000485131c73a24eff2186e4abe070d",
					"width": 64
				}
			],
			"popularity": 38,
			"date": "2011-08-25",
			"duration": 6.57,
			"url": "https://open.spotify.com/track/4vHi9eTIa4XDHBGez4dNB8",
			"id": "4vHi9eTIa4XDHBGez4dNB8"
		},
		{
			"music": "Scene Eight: The Spirit Carries On",
			"artist": "Dream Theater",
			"album": "Metropolis, Pt. 2: Scenes from a Memory",
			"images": [
				{
					"height": 640,
					"url": "https://i.scdn.co/image/ab67616d0000b273dbb83b10ff18df1213b76ac5",
					"width": 640
				},
				{
					"height": 300,
					"url": "https://i.scdn.co/image/ab67616d00001e02dbb83b10ff18df1213b76ac5",
					"width": 300
				},
				{
					"height": 64,
					"url": "https://i.scdn.co/image/ab67616d00004851dbb83b10ff18df1213b76ac5",
					"width": 64
				}
			],
			"popularity": 56,
			"date": "1999-01-01",
			"duration": 6.38,
			"url": "https://open.spotify.com/track/7ycz6sgZWp4wvF53BZVTjE",
			"id": "7ycz6sgZWp4wvF53BZVTjE"
		},
		{
			"music": "Cruz (22)",
			"artist": "Graça",
			"album": "Saltério",
			"images": [
				{
					"height": 640,
					"url": "https://i.scdn.co/image/ab67616d0000b27304d24f827deb1ccbbf4e3eac",
					"width": 640
				},
				{
					"height": 300,
					"url": "https://i.scdn.co/image/ab67616d00001e0204d24f827deb1ccbbf4e3eac",
					"width": 300
				},
				{
					"height": 64,
					"url": "https://i.scdn.co/image/ab67616d0000485104d24f827deb1ccbbf4e3eac",
					"width": 64
				}
			],
			"popularity": 3,
			"date": "2021-12-24",
			"duration": 6.28,
			"url": "https://open.spotify.com/track/7rLKeEfZagdBwK3dLQ32VR",
			"id": "7rLKeEfZagdBwK3dLQ32VR"
		},
		{
			"music": "Scene Five: Through Her Eyes",
			"artist": "Dream Theater",
			"album": "Metropolis, Pt. 2: Scenes from a Memory",
			"images": [
				{
					"height": 640,
					"url": "https://i.scdn.co/image/ab67616d0000b273dbb83b10ff18df1213b76ac5",
					"width": 640
				},
				{
					"height": 300,
					"url": "https://i.scdn.co/image/ab67616d00001e02dbb83b10ff18df1213b76ac5",
					"width": 300
				},
				{
					"height": 64,
					"url": "https://i.scdn.co/image/ab67616d00004851dbb83b10ff18df1213b76ac5",
					"width": 64
				}
			],
			"popularity": 48,
			"date": "1999-01-01",
			"duration": 5.29,
			"url": "https://open.spotify.com/track/19CegINw7X0pqHaY7YOaz8",
			"id": "19CegINw7X0pqHaY7YOaz8"
		},
		{
			"music": "Esmeralda Type",
			"artist": "UCLÃ",
			"album": "Esmeralda Type",
			"images": [
				{
					"height": 640,
					"url": "https://i.scdn.co/image/ab67616d0000b27327775e7e2deccac1f9bba204",
					"width": 640
				},
				{
					"height": 300,
					"url": "https://i.scdn.co/image/ab67616d00001e0227775e7e2deccac1f9bba204",
					"width": 300
				},
				{
					"height": 64,
					"url": "https://i.scdn.co/image/ab67616d0000485127775e7e2deccac1f9bba204",
					"width": 64
				}
			],
			"popularity": 28,
			"date": "2021-04-01",
			"duration": 4.52,
			"url": "https://open.spotify.com/track/0xIDhJUU1i3htOAq05O7fa",
			"id": "0xIDhJUU1i3htOAq05O7fa"
		},
		{
			"music": "Ouro Rosé",
			"artist": "UCLÃ",
			"album": "Ouro Rosé",
			"images": [
				{
					"height": 640,
					"url": "https://i.scdn.co/image/ab67616d0000b2739a23050ce79fe33f642360ba",
					"width": 640
				},
				{
					"height": 300,
					"url": "https://i.scdn.co/image/ab67616d00001e029a23050ce79fe33f642360ba",
					"width": 300
				},
				{
					"height": 64,
					"url": "https://i.scdn.co/image/ab67616d000048519a23050ce79fe33f642360ba",
					"width": 64
				}
			],
			"popularity": 45,
			"date": "2021-01-21",
			"duration": 4.5,
			"url": "https://open.spotify.com/track/6keP0AfCE5v4CTI1E5nrLv",
			"id": "6keP0AfCE5v4CTI1E5nrLv"
		},
		{
			"music": "Ladrão de Lágrimas - Acústico",
			"artist": "UCLÃ",
			"album": "Acústico Duzz",
			"images": [
				{
					"height": 640,
					"url": "https://i.scdn.co/image/ab67616d0000b273f89a145f534cfa632b0ce5fe",
					"width": 640
				},
				{
					"height": 300,
					"url": "https://i.scdn.co/image/ab67616d00001e02f89a145f534cfa632b0ce5fe",
					"width": 300
				},
				{
					"height": 64,
					"url": "https://i.scdn.co/image/ab67616d00004851f89a145f534cfa632b0ce5fe",
					"width": 64
				}
			],
			"popularity": 42,
			"date": "2019-05-30",
			"duration": 4.38,
			"url": "https://open.spotify.com/track/2a2yQU0uIbhjvuE1IpGNqX",
			"id": "2a2yQU0uIbhjvuE1IpGNqX"
		},
		{
			"music": "Another Day",
			"artist": "Dream Theater",
			"album": "Images and Words",
			"images": [
				{
					"height": 640,
					"url": "https://i.scdn.co/image/ab67616d0000b273f4d11b78efa76496f2acd618",
					"width": 640
				},
				{
					"height": 300,
					"url": "https://i.scdn.co/image/ab67616d00001e02f4d11b78efa76496f2acd618",
					"width": 300
				},
				{
					"height": 64,
					"url": "https://i.scdn.co/image/ab67616d00004851f4d11b78efa76496f2acd618",
					"width": 64
				}
			],
			"popularity": 57,
			"date": "1992-06-30",
			"duration": 4.23,
			"url": "https://open.spotify.com/track/69kZsoRrSf7GBTSdJ4BjqA",
			"id": "69kZsoRrSf7GBTSdJ4BjqA"
		},
		{
			"music": "Lobo-Guará",
			"artist": "UCLÃ",
			"album": "Lobo-Guará",
			"images": [
				{
					"height": 640,
					"url": "https://i.scdn.co/image/ab67616d0000b273adf672888af480c5cc9d0a87",
					"width": 640
				},
				{
					"height": 300,
					"url": "https://i.scdn.co/image/ab67616d00001e02adf672888af480c5cc9d0a87",
					"width": 300
				},
				{
					"height": 64,
					"url": "https://i.scdn.co/image/ab67616d00004851adf672888af480c5cc9d0a87",
					"width": 64
				}
			],
			"popularity": 47,
			"date": "2020-10-01",
			"duration": 4.22,
			"url": "https://open.spotify.com/track/6pPPjzQCW3TauculUPjKDs",
			"id": "6pPPjzQCW3TauculUPjKDs"
		},
		{
			"music": "Carta de Despedida",
			"artist": "Sueth",
			"album": "Má Influência",
			"images": [
				{
					"height": 640,
					"url": "https://i.scdn.co/image/ab67616d0000b273f45f52fa262c2ac258381f0b",
					"width": 640
				},
				{
					"height": 300,
					"url": "https://i.scdn.co/image/ab67616d00001e02f45f52fa262c2ac258381f0b",
					"width": 300
				},
				{
					"height": 64,
					"url": "https://i.scdn.co/image/ab67616d00004851f45f52fa262c2ac258381f0b",
					"width": 64
				}
			],
			"popularity": 32,
			"date": "2020-08-20",
			"duration": 3.36,
			"url": "https://open.spotify.com/track/38SxwpYb8bHZb68ihx3O2T",
			"id": "38SxwpYb8bHZb68ihx3O2T"
		},
		{
			"music": "Teofania (50)",
			"artist": "Graça",
			"album": "Saltério",
			"images": [
				{
					"height": 640,
					"url": "https://i.scdn.co/image/ab67616d0000b27304d24f827deb1ccbbf4e3eac",
					"width": 640
				},
				{
					"height": 300,
					"url": "https://i.scdn.co/image/ab67616d00001e0204d24f827deb1ccbbf4e3eac",
					"width": 300
				},
				{
					"height": 64,
					"url": "https://i.scdn.co/image/ab67616d0000485104d24f827deb1ccbbf4e3eac",
					"width": 64
				}
			],
			"popularity": 4,
			"date": "2021-12-24",
			"duration": 3.29,
			"url": "https://open.spotify.com/track/49RMsjt6xIDVy6kILWeso0",
			"id": "49RMsjt6xIDVy6kILWeso0"
		},
		{
			"music": "Bo Jack - Acústico",
			"artist": "UCLÃ",
			"album": "Acústico Duzz",
			"images": [
				{
					"height": 640,
					"url": "https://i.scdn.co/image/ab67616d0000b273f89a145f534cfa632b0ce5fe",
					"width": 640
				},
				{
					"height": 300,
					"url": "https://i.scdn.co/image/ab67616d00001e02f89a145f534cfa632b0ce5fe",
					"width": 300
				},
				{
					"height": 64,
					"url": "https://i.scdn.co/image/ab67616d00004851f89a145f534cfa632b0ce5fe",
					"width": 64
				}
			],
			"popularity": 42,
			"date": "2019-05-30",
			"duration": 3.28,
			"url": "https://open.spotify.com/track/0JDxvgzUHwZ7cYHXK3fb8V",
			"id": "0JDxvgzUHwZ7cYHXK3fb8V"
		},
		{
			"music": "Lágrimas em Poças",
			"artist": "Duzz",
			"album": "Lágrimas em Poças",
			"images": [
				{
					"height": 640,
					"url": "https://i.scdn.co/image/ab67616d0000b2730c49f33be5aada655d551b8c",
					"width": 640
				},
				{
					"height": 300,
					"url": "https://i.scdn.co/image/ab67616d00001e020c49f33be5aada655d551b8c",
					"width": 300
				},
				{
					"height": 64,
					"url": "https://i.scdn.co/image/ab67616d000048510c49f33be5aada655d551b8c",
					"width": 64
				}
			],
			"popularity": 39,
			"date": "2019-06-20",
			"duration": 3.25,
			"url": "https://open.spotify.com/track/4jVaJ3HJ8PXRLo3kO2sdgA",
			"id": "4jVaJ3HJ8PXRLo3kO2sdgA"
		},
		{
			"music": "Aquecendo a Nave",
			"artist": "Duzz",
			"album": "Aquecendo a Nave",
			"images": [
				{
					"height": 640,
					"url": "https://i.scdn.co/image/ab67616d0000b273e9a3c9a21db79deba305523c",
					"width": 640
				},
				{
					"height": 300,
					"url": "https://i.scdn.co/image/ab67616d00001e02e9a3c9a21db79deba305523c",
					"width": 300
				},
				{
					"height": 64,
					"url": "https://i.scdn.co/image/ab67616d00004851e9a3c9a21db79deba305523c",
					"width": 64
				}
			],
			"popularity": 30,
			"date": "2020-09-10",
			"duration": 3.25,
			"url": "https://open.spotify.com/track/2JkZoV2MoMh3LpFNgqTtrX",
			"id": "2JkZoV2MoMh3LpFNgqTtrX"
		},
		{
			"music": "Metamorfose Avalanche",
			"artist": "Duzz",
			"album": "Aquecendo a Nave",
			"images": [
				{
					"height": 640,
					"url": "https://i.scdn.co/image/ab67616d0000b273e9a3c9a21db79deba305523c",
					"width": 640
				},
				{
					"height": 300,
					"url": "https://i.scdn.co/image/ab67616d00001e02e9a3c9a21db79deba305523c",
					"width": 300
				},
				{
					"height": 64,
					"url": "https://i.scdn.co/image/ab67616d00004851e9a3c9a21db79deba305523c",
					"width": 64
				}
			],
			"popularity": 37,
			"date": "2020-09-10",
			"duration": 3.24,
			"url": "https://open.spotify.com/track/4LkR0WEiMkc7vh0TTgMJCV",
			"id": "4LkR0WEiMkc7vh0TTgMJCV"
		},
		{
			"music": "Scarface",
			"artist": "Duzz",
			"album": "Scarface",
			"images": [
				{
					"height": 640,
					"url": "https://i.scdn.co/image/ab67616d0000b2730ac549b5e3f04d88053c2da6",
					"width": 640
				},
				{
					"height": 300,
					"url": "https://i.scdn.co/image/ab67616d00001e020ac549b5e3f04d88053c2da6",
					"width": 300
				},
				{
					"height": 64,
					"url": "https://i.scdn.co/image/ab67616d000048510ac549b5e3f04d88053c2da6",
					"width": 64
				}
			],
			"popularity": 38,
			"date": "2019-09-23",
			"duration": 2.51,
			"url": "https://open.spotify.com/track/0yWOXAzS7XhGzvW1dJu2cE",
			"id": "0yWOXAzS7XhGzvW1dJu2cE"
		},
		{
			"music": "Missão Tom Cruise",
			"artist": "Duzz",
			"album": "Missão Tom Cruise",
			"images": [
				{
					"height": 640,
					"url": "https://i.scdn.co/image/ab67616d0000b2739a3ac1179da23e62336fe96b",
					"width": 640
				},
				{
					"height": 300,
					"url": "https://i.scdn.co/image/ab67616d00001e029a3ac1179da23e62336fe96b",
					"width": 300
				},
				{
					"height": 64,
					"url": "https://i.scdn.co/image/ab67616d000048519a3ac1179da23e62336fe96b",
					"width": 64
				}
			],
			"popularity": 35,
			"date": "2019-07-29",
			"duration": 2.47,
			"url": "https://open.spotify.com/track/0gqrai01ITJwJkrJa74Aex",
			"id": "0gqrai01ITJwJkrJa74Aex"
		},
		{
			"music": "Kurt Cobain - Acústico",
			"artist": "UCLÃ",
			"album": "Acústico Duzz",
			"images": [
				{
					"height": 640,
					"url": "https://i.scdn.co/image/ab67616d0000b273f89a145f534cfa632b0ce5fe",
					"width": 640
				},
				{
					"height": 300,
					"url": "https://i.scdn.co/image/ab67616d00001e02f89a145f534cfa632b0ce5fe",
					"width": 300
				},
				{
					"height": 64,
					"url": "https://i.scdn.co/image/ab67616d00004851f89a145f534cfa632b0ce5fe",
					"width": 64
				}
			],
			"popularity": 49,
			"date": "2019-05-30",
			"duration": 2.45,
			"url": "https://open.spotify.com/track/5rNHchF00RDf45YhWXBBOX",
			"id": "5rNHchF00RDf45YhWXBBOX"
		},
		{
			"music": "Remédio e Soda",
			"artist": "Duzz",
			"album": "Remédio e Soda",
			"images": [
				{
					"height": 640,
					"url": "https://i.scdn.co/image/ab67616d0000b273bf35151c9bd76b46acc0d00f",
					"width": 640
				},
				{
					"height": 300,
					"url": "https://i.scdn.co/image/ab67616d00001e02bf35151c9bd76b46acc0d00f",
					"width": 300
				},
				{
					"height": 64,
					"url": "https://i.scdn.co/image/ab67616d00004851bf35151c9bd76b46acc0d00f",
					"width": 64
				}
			],
			"popularity": 34,
			"date": "2021-03-22",
			"duration": 2.37,
			"url": "https://open.spotify.com/track/47ecSPAKNzGrQpjjmycHb6",
			"id": "47ecSPAKNzGrQpjjmycHb6"
		}
	],
	"additional": {
		"albuns": {
			"Acústico Duzz": 3,
			"Saltério": 2,
			"Metropolis, Pt. 2: Scenes from a Memory": 2,
			"Aquecendo a Nave": 2,
			"Lágrimas em Poças": 1,
			"Lobo-Guará": 1,
			"Black Clouds & Silver Linings": 1,
			"Ouro Rosé": 1,
			"Scarface": 1,
			"A Dramatic Turn of Events": 1,
			"Esmeralda Type": 1,
			"Missão Tom Cruise": 1,
			"Remédio e Soda": 1,
			"Má Influência": 1,
			"Images and Words": 1
		},
		"artists": {
			"Duzz": 6,
			"UCLÃ": 6,
			"Dream Theater": 5,
			"Graça": 2,
			"Sueth": 1
		},
		"decades": {
			"count": {
				"2020": 9,
				"2010": 7,
				"1990": 3,
				"2000": 1
			},
			"popularity": [
				{
					"decade": 1990,
					"mean": 53.666666666666664,
					"mode": 56,
					"median": 56
				},
				{
					"decade": 2020,
					"mean": 28.88888888888889,
					"mode": 47,
					"median": 32
				},
				{
					"decade": 2000,
					"mean": 41,
					"mode": 41,
					"median": 41
				},
				{
					"decade": 2010,
					"mean": 40.42857142857143,
					"mode": 42,
					"median": 39
				}
			]
		},
		"popularity": {
			"mean": 37.25,
			"mode": 42,
			"median": 38.5
		},
		"duration": {
			"mean": 4.38,
			"median": 3.59,
			"mode": 3.25
		}
	},
	"features": {
		"acousticness": {
			"Lágrimas em Poças": 0.306,
			"Lobo-Guará": 0.267,
			"Cruz (22)": 0.87,
			"Scene Eight: The Spirit Carries On": 0.293,
			"Ladrão de Lágrimas - Acústico": 0.275,
			"The Best of Times": 0.000858,
			"Scene Five: Through Her Eyes": 0.747,
			"Ouro Rosé": 0.144,
			"Bo Jack - Acústico": 0.438,
			"Scarface": 0.2,
			"Teofania (50)": 0.288,
			"This Is the Life": 0.146,
			"Esmeralda Type": 0.0223,
			"Missão Tom Cruise": 0.083,
			"Kurt Cobain - Acústico": 0.283,
			"Metamorfose Avalanche": 0.133,
			"Remédio e Soda": 0.231,
			"Carta de Despedida": 0.00608,
			"Another Day": 0.00223,
			"Aquecendo a Nave": 0.0185
		},
		"danceability": {
			"Lágrimas em Poças": 0.464,
			"Lobo-Guará": 0.84,
			"Cruz (22)": 0.308,
			"Scene Eight: The Spirit Carries On": 0.321,
			"Ladrão de Lágrimas - Acústico": 0.769,
			"The Best of Times": 0.204,
			"Scene Five: Through Her Eyes": 0.593,
			"Ouro Rosé": 0.826,
			"Bo Jack - Acústico": 0.688,
			"Scarface": 0.809,
			"Teofania (50)": 0.286,
			"This Is the Life": 0.246,
			"Esmeralda Type": 0.862,
			"Missão Tom Cruise": 0.736,
			"Kurt Cobain - Acústico": 0.766,
			"Metamorfose Avalanche": 0.832,
			"Remédio e Soda": 0.705,
			"Carta de Despedida": 0.838,
			"Another Day": 0.454,
			"Aquecendo a Nave": 0.811
		},
		"energy": {
			"Lágrimas em Poças": 0.573,
			"Lobo-Guará": 0.492,
			"Cruz (22)": 0.384,
			"Scene Eight: The Spirit Carries On": 0.544,
			"Ladrão de Lágrimas - Acústico": 0.699,
			"The Best of Times": 0.719,
			"Scene Five: Through Her Eyes": 0.324,
			"Ouro Rosé": 0.535,
			"Bo Jack - Acústico": 0.601,
			"Scarface": 0.477,
			"Teofania (50)": 0.836,
			"This Is the Life": 0.566,
			"Esmeralda Type": 0.509,
			"Missão Tom Cruise": 0.67,
			"Kurt Cobain - Acústico": 0.703,
			"Metamorfose Avalanche": 0.491,
			"Remédio e Soda": 0.687,
			"Carta de Despedida": 0.487,
			"Another Day": 0.614,
			"Aquecendo a Nave": 0.337
		},
		"instrumentalness": {
			"Lágrimas em Poças": 0,
			"Lobo-Guará": 0,
			"Cruz (22)": 5.88e-06,
			"Scene Eight: The Spirit Carries On": 1.11e-05,
			"Ladrão de Lágrimas - Acústico": 5.13e-06,
			"The Best of Times": 0.0139,
			"Scene Five: Through Her Eyes": 3.3e-06,
			"Ouro Rosé": 0,
			"Bo Jack - Acústico": 0,
			"Scarface": 2.67e-06,
			"Teofania (50)": 1.97e-05,
			"This Is the Life": 0.00127,
			"Esmeralda Type": 1.72e-06,
			"Missão Tom Cruise": 0,
			"Kurt Cobain - Acústico": 3.63e-05,
			"Metamorfose Avalanche": 0.000144,
			"Remédio e Soda": 2.14e-05,
			"Carta de Despedida": 0,
			"Another Day": 1.16e-05,
			"Aquecendo a Nave": 6.2e-05
		},
		"liveness": {
			"Lágrimas em Poças": 0.171,
			"Lobo-Guará": 0.0814,
			"Cruz (22)": 0.116,
			"Scene Eight: The Spirit Carries On": 0.11,
			"Ladrão de Lágrimas - Acústico": 0.0798,
			"The Best of Times": 0.136,
			"Scene Five: Through Her Eyes": 0.498,
			"Ouro Rosé": 0.116,
			"Bo Jack - Acústico": 0.128,
			"Scarface": 0.102,
			"Teofania (50)": 0.431,
			"This Is the Life": 0.126,
			"Esmeralda Type": 0.107,
			"Missão Tom Cruise": 0.149,
			"Kurt Cobain - Acústico": 0.153,
			"Metamorfose Avalanche": 0.0792,
			"Remédio e Soda": 0.113,
			"Carta de Despedida": 0.188,
			"Another Day": 0.0936,
			"Aquecendo a Nave": 0.21
		},
		"valence": {
			"Lágrimas em Poças": 0.252,
			"Lobo-Guará": 0.545,
			"Cruz (22)": 0.101,
			"Scene Eight: The Spirit Carries On": 0.283,
			"Ladrão de Lágrimas - Acústico": 0.298,
			"The Best of Times": 0.13,
			"Scene Five: Through Her Eyes": 0.156,
			"Ouro Rosé": 0.544,
			"Bo Jack - Acústico": 0.314,
			"Scarface": 0.233,
			"Teofania (50)": 0.322,
			"This Is the Life": 0.149,
			"Esmeralda Type": 0.458,
			"Missão Tom Cruise": 0.744,
			"Kurt Cobain - Acústico": 0.283,
			"Metamorfose Avalanche": 0.513,
			"Remédio e Soda": 0.251,
			"Carta de Despedida": 0.446,
			"Another Day": 0.343,
			"Aquecendo a Nave": 0.456
		}
	}
}

```
## Como executar a API?
Para executar a API precisa ter o Docker instalado. Após instalar o Docker faça:

```bash
sudo docker build . -f Dockerfile --tag=api-tcc
```
E após isso:
```bash
sudo docker run -d --name tcc-container -p 8000:80 api-tcc
```

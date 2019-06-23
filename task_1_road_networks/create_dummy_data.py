import io
import json

road_network = {
    "graph": {
        "nodes": [
            {
                "id": 0
            },
            {
                "id": 1
            },
            {
                "id": 2
            },
            {
                "id": 3
            },
            {
                "id": 4
            },
            {
                "id": 5
            },
            {
                "id": 6
            },
            {
                "id": 7
            },
            {
                "id": 8
            }
        ],

        "edges": [
            {
                "source": 0,
                "target": 3,
                "weight": 3,
                "directed": False,
                "orientation": "S"
            },

            {
                "source": 1,
                "target": 4,
                "weight": 2,
                "directed": False,
                "orientation": "S"
            },

            {
                "source": 2,
                "target": 3,
                "weight": 3,
                "directed": False,
                "orientation": "W"
            },

            {
                "source": 3,
                "target": 1,
                "weight": 2,
                "directed": True,
                "orientation": "NE"
            },

            {
                "source": 3,
                "target": 4,
                "weight": 6,
                "directed": False,
                "orientation": "E"
            },

            {
                "source": 3,
                "target": 6,
                "weight": 2,
                "directed": True,
                "orientation": "S"
            },

            {
                "source": 4,
                "target": 6,
                "weight": 4,
                "directed": False,
                "orientation": "E"
            },

            {
                "source": 4,
                "target": 8,
                "weight": 1,
                "directed": False,
                "orientation": "SE"
            },

            {
                "source": 7,
                "target": 4,
                "weight": 3,
                "directed": True,
                "orientation": "N"
            }

        ]
    }
}

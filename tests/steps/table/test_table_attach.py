from frictionless import Resource, Pipeline, Step, steps


# General


def test_step_table_attach():
    source = Resource("data/transform.csv")
    pipeline = Pipeline(
        steps=[
            steps.table_attach(resource=Resource(data=[["note"], ["large"], ["mid"]]))
        ],
    )
    target = source.transform(pipeline)
    assert target.schema.to_descriptor() == {
        "fields": [
            {"name": "id", "type": "integer"},
            {"name": "name", "type": "string"},
            {"name": "population", "type": "integer"},
            {"name": "note", "type": "string"},
        ]
    }
    assert target.read_rows() == [
        {"id": 1, "name": "germany", "population": 83, "note": "large"},
        {"id": 2, "name": "france", "population": 66, "note": "mid"},
        {"id": 3, "name": "spain", "population": 47, "note": None},
    ]


def test_step_table_attach_from_descriptor():
    source = Resource("data/transform.csv")
    pipeline = Pipeline(
        steps=[
            Step.from_descriptor(
                {
                    "type": "table-attach",
                    "resource": dict(data=[["note"], ["large"], ["mid"]]),
                }
            ),
        ],
    )
    target = source.transform(pipeline)
    assert target.schema.to_descriptor() == {
        "fields": [
            {"name": "id", "type": "integer"},
            {"name": "name", "type": "string"},
            {"name": "population", "type": "integer"},
            {"name": "note", "type": "string"},
        ]
    }
    assert target.read_rows() == [
        {"id": 1, "name": "germany", "population": 83, "note": "large"},
        {"id": 2, "name": "france", "population": 66, "note": "mid"},
        {"id": 3, "name": "spain", "population": 47, "note": None},
    ]

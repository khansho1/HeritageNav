
import csv
import io
import json


def sites_to_csv(sites):

    output = io.StringIO()
    writer = csv.writer(output)

    writer.writerow([
        "id",
        "name",
        "city",
        "state",
        "description"
    ])

    writer.writerows(sites)

    return output.getvalue()


def sites_to_json(sites):

    data = []

    for site in sites:

        data.append({
            "id": site[0],
            "name": site[1],
            "city": site[2],
            "state": site[3],
            "description": site[4]
        })

    return json.dumps(
        data,
        indent=4,
        ensure_ascii=False
    )


def read_csv_file(uploaded_file):

    content = uploaded_file.getvalue().decode("utf-8-sig")

    reader = csv.DictReader(io.StringIO(content))

    required_columns = {
        "name",
        "city",
        "state",
        "description"
    }

    if not required_columns.issubset(
        set(reader.fieldnames or [])
    ):
        raise ValueError(
            "CSV must contain name, city, state and description columns."
        )

    return list(reader)


def read_json_file(uploaded_file):

    data = json.load(uploaded_file)

    if not isinstance(data, list):
        raise ValueError("JSON must contain a list of records.")

    return data

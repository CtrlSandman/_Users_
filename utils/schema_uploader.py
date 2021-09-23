from confluent_kafka import avro


class SchemaUploader:

    @staticmethod
    def load_avro_schema(schema_file: str) -> tuple:
        key_schema_str = '{"type":"string"}'

        key_schema = avro.loads(key_schema_str)
        value_schema = avro.load(f"./schema/{schema_file}")

        return key_schema, value_schema

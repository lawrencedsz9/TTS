from TTS.api import TTS

# List all available models
print("Available TTS Models:")
print("-------------------")
tts = TTS()
models = tts.list_models()

# Print model information
for model_type in models.models_dict:
    print(f"\nModel Type: {model_type}")
    for lang in models.models_dict[model_type]:
        print(f"  Language: {lang}")
        for dataset in models.models_dict[model_type][lang]:
            print(f"    Dataset: {dataset}")
            for model in models.models_dict[model_type][lang][dataset]:
                print(f"      - {model}") 
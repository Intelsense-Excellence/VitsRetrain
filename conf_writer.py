sample_text = "এইচআর টেক্সটাইল বাংলাদেশের ভেতরে একাধিক আউটলেটের মাধ্যমে শাড়ি বাচ্চাদের পোশাক মহিলাদের পোশাক এবং অন্যান্য টেক্সটাইল পণ্য উৎপাদন ও বিপণন করে"


vits_ft_config = {
    "project_name": "mms_bengali_finetuning",
    "push_to_hub": True,
    "hub_model_id": "intelsense/vits_hf_bn_openslr_v1",
    "report_to": ["wandb"],
    "overwrite_output_dir": True,
    "output_dir": "./tmp/vits_finetuned_ben",

    "dataset_name": "intelsense/openslr_male_tts_mono_bd",    
    # "dataset_config_name": "male", 
    "audio_column_name": "audio", 
    "text_column_name":"text",
    "train_split_name": "train",
    "eval_split_name": "val",
    # "speaker_id_column_name": "speaker_id",
    "override_speaker_embeddings": True,
    # "filter_on_speaker_id": 0,

    "hub_private_repo": True,
    "hub_token": "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",

    "full_generation_sample_text": sample_text,
    
    "max_duration_in_seconds": 20,
    "min_duration_in_seconds": 1.0,
    "max_tokens_length": 500,

    "model_name_or_path": "intelsense/mms-tts-ben",

    "preprocessing_num_workers": 1,

    "do_train": True,
    "num_train_epochs": 300,
    "gradient_accumulation_steps": 1,
    "gradient_checkpointing": False,
    "per_device_train_batch_size": 128,
    "learning_rate": 2e-5,
    "adam_beta1": 0.8,
    "adam_beta2": 0.99,
    "warmup_ratio": 0.01,
    "group_by_length": False,

    "do_eval": True, 
    "eval_steps": 50,
    "per_device_eval_batch_size": 128,
    "max_eval_samples": 25, 
    "do_step_schedule_per_epoch": True,

    "weight_disc": 3,
    "weight_fmaps": 1,
    "weight_gen": 1,
    "weight_kl": 1.5,
    "weight_duration": 1,
    "weight_mel": 35,

    "fp16": True,
    "seed": 456
}


import json

with open('./finetune_ben.json', 'w') as f:
    json.dump(vits_ft_config, f, indent=4, ensure_ascii=False)
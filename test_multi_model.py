from ai_engine.multi_model_service import multi_model_service
from ai_engine.colab_engine import colab_ai_engine
from PIL import Image

sample_img = Image.open('static/samples/sample_tomato_early_blight.jpg')
assert colab_ai_engine.is_loaded, colab_ai_engine.load_error

print('--- Test Model 1 ---')
m1_res = multi_model_service.predict(sample_img, model_id='model_1')
print('Model 1:', m1_res['selected_model']['name'], '->', m1_res['prediction']['disease'], f"({m1_res['prediction']['confidence']}%)")

print('--- Test Model 2 (Colab) ---')
m2_res = multi_model_service.predict(sample_img, model_id='model_2')
assert m2_res['selected_model']['id'] == 'model_2'
assert m2_res['prediction']['class_key'] in colab_ai_engine.class_mapping.values()
assert 0 <= m2_res['prediction']['confidence'] <= 100
print('Model 2:', m2_res['selected_model']['name'], '->', m2_res['prediction']['disease'], f"({m2_res['prediction']['confidence']}%)")

print('--- Test Dual Comparison ---')
cmp_res = multi_model_service.predict(sample_img, model_id='compare')
print('Comparison Consensus:', cmp_res['comparison']['status'])
print('Agreement:', cmp_res['comparison']['is_agreement'])
print('Model 1 Prediction:', cmp_res['comparison']['model_1_prediction'])
print('Model 2 Prediction:', cmp_res['comparison']['model_2_prediction'])

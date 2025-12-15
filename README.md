# **전체 구현 로드맵 (Top-level)**

프레임워크는 7개의 모듈로 구성

1. **Data Profiler**
2. **Model Family Selector**
3. **Architecture Template Generator**
4. **Search Engine (AutoML/NAS)**
5. **Evaluator**
6. **Decision Agent**
7. **Architecture Converter (선택적)**
8. **Orchestrator (전체 실행기)**

각 모듈은 **하나의 책임만 수행**, 독립적으로 테스트


# **전체 구현 순서**

1. **데이터 구조 + DataProfiler**
2. **ModelFamilySelector**
3. **TemplateGenerator**
4. **LSTM/Transformer 모델 구현(전이학습 사용)**
5. **SearchEngine(Random Search)**
6. **Evaluator**
7. **DecisionAgent**
8. **Orchestrator**
9. **ArchitectureConverter**
10. **전체 통합 테스트**
---

# 1\. Data Profiler — “데이터 특징 뽑기”

### 목표

시계열 데이터를 보고 **숫자 기반 특징(MetaFeatures)** 추출한다.

### 

### 구현 계획

* `TimeSeriesDataset` 클래스 정의
* `MetaFeatures` 데이터 클래스 정의
* `SimpleStatDataProfiler` 구현
    - 길이, 변수 수
    - missing 비율
    - 간단한 계절성/추세 지표
    - 노이즈 레벨 근사치



## 산출물

* `MetaFeatures` 객체
* 단위 테스트: 여러 데이터셋에 대해 메타 특성 출력


---

# 2\. Model Family Selector — “LSTM/Transformer/Hybrid 선택”

### 목표

메타 특성을 보고 **어떤 모델 계열이 적합한지 자동 선택**.



### 구현 계획

* `ModelFamily` enum 정의
* `RuleBasedFamilySelector` 구현
    - 길이, 데이터 양, 계절성 기반 간단 규칙
* (선택) 나중에 ML 기반 selector로 확장



### 산출물

* `ModelFamily` 값 하나
* 단위 테스트: 다양한 MetaFeatures 입력 → 올바른 패밀리 선택


---

# 3\. Architecture Template Generator — “모델 뼈대 만들기”

### 목표

선택된 모델 계열에 맞는 **기본 config + 탐색 범위(search space)** 생성.



### 구현 계획

* `ModelTemplate` 데이터 클래스 정의
* `DefaultArchTemplateGenerator` 구현
    - LSTM 템플릿
    - Transformer 템플릿
    - Hybrid 템플릿



### 산출물

* `ModelTemplate(base_config, search_space)`
* 단위 테스트: family별 템플릿 생성 확인
---

# 4\. Search Engine — “여러 모델 자동 생성·학습”

### 목표

템플릿 기반으로 다양한 config를 샘플링하고,
각 config로 모델을 학습해 **후보 모델 리스트** 생성.



### 구현 계획

* PyTorch 기반 LSTM 모델 구현
* PyTorch 기반 Transformer 모델 구현
* `RandomSearchEngine` 구현
    - config 샘플링
    - 모델 생성
    - 학습 루프
    - 후보 모델 저장



### 산출물

* `List[TrainedCandidate]`
* 단위 테스트: 작은 데이터셋에서 2~3개 후보 생성
---

# 5\. Evaluator — “성능 측정”

### 목표

각 후보 모델을 동일한 방식으로 평가해 **metrics + latency**를 반환.

### 구현 계획

* `EvaluationResult` 데이터 클래스
* `StandardEvaluator` 구현
    - MAE, RMSE
    - latency 측정
    - 메모리 사용량(optional)



### 산출물

* `EvaluationResult` 리스트
* 단위 테스트: 후보 모델에 대해 metric 계산
---

# 6\. Decision Agent — “최종 모델 선택”

### 목표

여러 평가 결과 중 **최고 모델 하나 선택**.



### 구현 계획

* `SimpleDecisionAgent` 구현
    - primary\_metric 기준 최소값 선택
* (선택) 나중에 RL 기반 policy로 확장 가능



### 산출물

* 최종 선택된 `EvaluationResult`
* 단위 테스트: metric 리스트에서 최저값 선택
---

# 7\. Architecture Converter — “LSTM → Transformer 자동 변환” (선택적)

### 목표

기존 LSTM 모델 구조를 읽어 Transformer 템플릿으로 변환.



### 구현 계획

`SimpleLSTMToTransformerConverter` 구현
  - hidden\_size → d\_model
  - num\_layers → num\_layers
  - dropout 그대로
  - head 수 자동 계산



### 산출물

* Transformer 템플릿
* 단위 테스트: LSTM 모델 입력 → Transformer 템플릿 출력

---

# 8\. Orchestrator — “전체 자동화 파이프라인”

### 목표

위의 모든 모듈을 연결해 **end-to-end 자동 모델 선택·탐색·평가** 수행.



### 구현 계획

* `TimeSeriesAutoFramework` 구현
    - profiler → selector → template → search → evaluate → decide
* 기존 LSTM 입력 시 converter 사용



### 산출물

* 최종 best 모델 + config
* 단위 테스트: toy dataset으로 end-to-end 실행
---



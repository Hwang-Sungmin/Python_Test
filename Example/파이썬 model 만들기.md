# 모델 매니저

- 모델 매니저
  - [디폴트 모델 매니저 = objects](https://wikidocs.net/6668#objects)
  - 커스텀 모델 매니저
    - 모델 매니저를 추가하는 방식
      - [커스템 모델 매니저를 정의한다.](https://wikidocs.net/6668#_4)
      - [모델에 커스텀 매니저를 추가한다.](https://wikidocs.net/6668#_5)
      - [커스텀 모델 매니저의 메소드 호출 예시](https://wikidocs.net/6668#_6)
    - 모델 매니저를 메소드 체인로 지정하는 방식
      - [커스템 모델 매니저를 정의한다.](https://wikidocs.net/6668#_8)
      - [모델의 기본 매니저를 커스텀 메소드로 변경한다.](https://wikidocs.net/6668#_9)
      - [커스텀 모델 매니저의 메소드 체인 호출 예시](https://wikidocs.net/6668#_10)
- [정리](https://wikidocs.net/6668#_11)
- [참고문헌](https://wikidocs.net/6668#_12)

# 모델 매니저

## 디폴트 모델 매니저 = objects

모델 매니저는 데이터베이스 쿼리와 연동되는 인터페이스이다.

각 모델은 애플리케이션에서 최소 하나의 매니저를 가진다. 디폴트 모델 매니저의 이름은 `objects`이다.

## 커스텀 모델 매니저

커스텀 모델 매니저를 구현하는 방법은 크게 두 가지이다.

- 모델 매니저를 매번 추가해서 특정 모델 매니저 인스턴스를 이용하는 방식
- 디폴트 모델 매니저를 변경 후 메소드 체인으로 호출하는 방식

### 모델 매니저를 추가하는 방식

#### 커스템 모델 매니저를 정의한다.

`blog/models.py` 파일에 추가

```
class PublishedManager(models.Manager):
    def get_queryset(self):
        return super(PublishedManager, self).get_queryset().filter(status='published')

```

#### 모델에 커스텀 매니저를 추가한다.

`blog/models.py` 파일 수정

```
class Post(models.Model):
    objects = models.Manager()
    published = PublishedManager()

    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )

    publish = models.DateTimeField(default=timezone.now)

    ... 생략 ...

```

#### 커스텀 모델 매니저의 메소드 호출 예시

```
>>> from blog.models import Post
>>> Post.objects.count()
2
>>> Post.published.count()
1

```

### 모델 매니저를 메소드 체인로 지정하는 방식

#### 커스템 모델 매니저를 정의한다.

`blog/models.py` 파일에 추가

```
class PublishedManager(models.Manager):
    use_for_related_fields = True

    def published(self, **kwargs):
        return self.filter(status='published', **kwargs)

```

`use_for_related_fields = True` 옵션은 기본 매니저로 이 매니저를 정의한 모델이 있을 때 이 모델을 가리키는 모든 관계 참조에서 모델 매니저를 사용할 수 있도록 한다.

#### 모델의 기본 매니저를 커스텀 메소드로 변경한다.

`blog/models.py` 파일 수정

```
class Post(models.Model):
    objects = PublishedManager()

    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )

    publish = models.DateTimeField(default=timezone.now)

    ... 생략 ...

```

#### 커스텀 모델 매니저의 메소드 체인 호출 예시

```
>>> from blog.models import Post
>>> Post.objects.count()
2
>>> Post.objects.published().count()
1

```


    assert_equals,
    assert_is_not,
)
import pickle
import copy


def test_model_definition_pickle():
    defn = model_definition(10, [bb, niw(3)])
    bstr = pickle.dumps(defn)
    defn1 = pickle.loads(bstr)
    assert_equals(defn.n(), defn1.n())
    assert_equals(len(defn.models()), len(defn1.models()))
    for a, b in zip(defn.models(), defn1.models()):
        assert_equals(a.name(), b.name())

def test_model_definition_copy():
    defn = model_definition(10, [bb, niw(3)])
    defn_shallow = copy.copy(defn)
    defn_deep = copy.deepcopy(defn)
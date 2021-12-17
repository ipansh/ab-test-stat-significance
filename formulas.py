import scipy
from scipy import stats
from scipy.stats import norm

def get_pvalue_student(mean_control, std_control, nobs_control, mean_test, std_test, nobs_test):
    return format(stats.ttest_ind_from_stats(mean_control, std_control, nobs_control, mean_test, std_test, nobs_test)[1],'.4f')

def get_pvalue_conversion(control_size,control_conversion,experiment_size,experiment_conversion):

  ### STEP1: calculate standard error for both groups
  def standard_error(sample_size, successes):
    p = float(successes) / sample_size
    return ((p * (1 - p)) / sample_size) ** 0.5

  ### STE2: calculate z-score
  def zscore(size_a, successes_a, size_b, successes_b):
    p_a = float(successes_a) / size_a
    p_b = float(successes_b) / size_b
    se_a = standard_error(size_a, successes_a)
    se_b = standard_error(size_b, successes_b)
    numerator = (p_b - p_a)
    denominator = (se_a ** 2 + se_b ** 2) ** 0.5
    return numerator / denominator

  ### STEP3: translated z-score to p-value
  def percentage_from_zscore(zscore):
    return norm.sf(abs(zscore))
    
  exp_zscore = zscore(control_size, control_conversion, experiment_size, experiment_conversion)
  
  return percentage_from_zscore(exp_zscore)
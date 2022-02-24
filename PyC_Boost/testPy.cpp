#include <boost/python.hpp>

char const* helw()
{
  return "hello world";
}

BOOST_PYTHON_MODULE(hello_ext)
{
  using namespace boost::python;
  def("hell",helw);
}

